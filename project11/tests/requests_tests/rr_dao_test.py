from daos.e_daos.e_daos import EDao
from daos.e_daos.e_daos_postgres import EDaoPostgres
from daos.r_request_daos.rr_dao import RrDao
from daos.r_request_daos.rr_postgres_dao import RrDaoPostgres
from exceptions.u_p_exception import UsernamePasswordNotMatch
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr

e_dao: EDao = EDaoPostgres()
rr_dao: RrDao = RrDaoPostgres()
rr_test: Rr = Rr(0,1000,"shopping","pending",1)


class TestRrDao:

    def tets_create_request(self):
        tested_rr = rr_dao.create_request(rr_test)
        assert tested_rr.rr_id != 0

    def test_get_all_requests_by_e_id(self):
        n = len(rr_dao.get_all_requests_by_e_id(1))
        rr_dao.create_request(rr_test)
        m = len(rr_dao.get_all_requests_by_e_id(1))
        assert (m-n) >=1

    def test_get_all_requests(self) -> [Rr]:
        n = len(rr_dao.get_all_requests())
        rr_dao.create_request(rr_test)
        m = len(rr_dao.get_all_requests())
        assert (m - n) >= 1


    def test_update_request(self):
        tested_rr = rr_dao.create_request(rr_test)
        rr_dao.update_request(tested_rr, "rejected")
        assert tested_rr.rr_status == "rejected"


    def test_get_request_by_rr_id(self) -> Rr:
        tested_rr = rr_dao.create_request(rr_test)
        tested_rr_1 = rr_dao.get_request_by_rr_id(tested_rr.rr_id)
        assert tested_rr_1.rr_id == tested_rr.rr_id


    def test_get_reports_by_statuses(self):
        m = rr_dao.get_reports_by_statuses("pending")
        rr_test1: Rr = Rr(0, 1000, "shopping", "pending", 1)
        rr_test1.rr_status = "pending"
        rr_dao.create_request(rr_test1)
        n = rr_dao.get_reports_by_statuses("pending")
        assert (n['count']-m['count']) >= 1




    def test_get_reports_for_all(self) -> dict:
        m = rr_dao.get_reports_for_all()
        rr_test1: Rr = Rr(0, 1000, "shopping", "pending", 1)
        rr_dao.create_request(rr_test1)
        n = rr_dao.get_reports_for_all()
        assert (n['count'] - m['count']) >= 1