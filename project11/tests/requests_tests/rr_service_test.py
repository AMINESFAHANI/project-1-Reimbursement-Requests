from daos.e_daos.e_daos import EDao
from daos.e_daos.e_daos_postgres import EDaoPostgres
from daos.r_request_daos.rr_dao import RrDao
from daos.r_request_daos.rr_postgres_dao import RrDaoPostgres
from exceptions.u_p_exception import UsernamePasswordNotMatch
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr
from services.rr_services.rr_service import RrService
from services.rr_services.rr_sevice_impl import RrServiceImpl

e_dao: EDao = EDaoPostgres()
rr_dao: RrDao = RrDaoPostgres()
rr_service: RrService = RrServiceImpl(rr_dao)
rr_test: Rr = Rr(0, 1000, "shopping", "pending", 1)


class TestRrService:

    def test_update_request(self):
        rr_test1 = rr_dao.create_request(rr_test)
        rr_test2 = rr_service.update_request(rr_test1.rr_id, "rejected")
        assert rr_test1.rr_status != rr_test2.rr_status and rr_test2.rr_status == "rejected"
