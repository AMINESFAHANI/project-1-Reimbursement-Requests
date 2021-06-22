from daos.e_daos.e_daos import EDao
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr
from exceptions.ResourceNotFoundError import ResourceNotFoundError
from exceptions.u_p_exception import UsernamePasswordNotMatch
from utils.connection_util import connection


class EDaoPostgres(EDao):
    def check_login_e_m(self, username: str, password: str) -> Employee or Manager:
        sql = "select * from employee where e_username =%s and e_password=%s;"
        cursor = connection.cursor()
        cursor.execute(sql, [username, password])
        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            employee = Employee(*record)
            return employee

        sql = "select * from manager where m_username =%s and m_password=%s ;"
        cursor = connection.cursor()
        cursor.execute(sql, [username, password])
        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            manager = Manager(*record)
            return manager
        raise UsernamePasswordNotMatch


