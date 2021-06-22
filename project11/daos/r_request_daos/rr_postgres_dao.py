from daos.e_daos.e_daos import EDao
from daos.r_request_daos.rr_dao import RrDao
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr
from exceptions.ResourceNotFoundError import ResourceNotFoundError
from exceptions.u_p_exception import UsernamePasswordNotMatch
from utils.connection_util import connection


class RrDaoPostgres(RrDao):

    def get_all_requests_by_e_id(self, rr_e_id: int) -> [Rr]:
        sql = """select * from rr where rr_e_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [rr_e_id])
        records = cursor.fetchall()
        requests = [Rr(*record) for record in records]
        if len(requests) == 0:
            raise ResourceNotFoundError
        return requests

    def create_request(self, rr: Rr) -> Rr:
        sql = """insert into rr (rr_amount,rr_reason,rr_status,rr_e_id) values (%s,%s,%s,%s) returning rr_id ;"""
        cursor = connection.cursor()
        cursor.execute(sql, [rr.rr_amount, rr.rr_reason, rr.rr_status, rr.rr_e_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        rr.rr_id = record[0]
        return rr

    def get_all_requests(self) -> [Rr]:
        sql = """select * from rr order by rr_status"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests = [Rr(*record) for record in records]
        if len(requests) == 0:
            raise ResourceNotFoundError
        return requests

    def update_request(self, rr: Rr, rr_status: str) -> Rr:
        sql = """update rr set rr_status = %s where rr_id = %s returning rr_status ;"""
        cursor = connection.cursor()
        cursor.execute(sql, [rr_status, rr.rr_id])
        connection.commit()
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        rr.rr_status = record[0]
        return rr

    def get_request_by_rr_id(self, rr_id: int) -> Rr:
        sql = """select * from rr where rr_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [rr_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        rr = Rr(*record)
        return rr

    def get_reports_by_statuses(self, statuses: str) -> dict:

        sql = """SELECT COUNT(rr_id),SUM(rr_amount),avg(rr_amount),max(rr_amount),min(rr_amount) FROM rr  where rr_status=%s;"""
        cursor = connection.cursor()
        cursor.execute(sql, [statuses])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        report = {"count": record[0], "sum": record[1], "average": int(record[2]), "max": record[3],
                  "min": record[4]}
        return report

    def get_reports_for_all(self) -> dict:

        sql = """SELECT COUNT(rr_id),SUM(rr_amount),avg(rr_amount),max(rr_amount),min(rr_amount) FROM rr;"""
        cursor = connection.cursor()
        cursor.execute(sql)
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError
        report = {"count": record[0], "sum": record[1], "average": int(record[2]), "max": record[3],
                  "min": record[4]}
        return report

    def get_reports_for_employee(self) -> [dict]:

        sql = """select * from (select e_id ,e_name ,sum(rr_amount)as total from employee,rr where rr.rr_e_id=employee.e_id group by e_id ,e_name) s order by  total DESC;"""

        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        if len(records) == 0:
            raise ResourceNotFoundError
        reports = []
        for record in records:
            report = {"eId": record[0], "eName": record[1], "amount": int(record[2])}
            reports.append(report)
        return reports
