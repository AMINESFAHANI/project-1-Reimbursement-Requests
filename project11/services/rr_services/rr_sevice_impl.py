from daos.e_daos.e_daos import EDao
from daos.r_request_daos.rr_dao import RrDao
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr
from services.e_services.e_service import EService
from services.rr_services.rr_service import RrService


class RrServiceImpl(RrService):

    def __init__(self, rr_dao: RrDao):
        self.rr_dao = rr_dao

    def get_all_requests_by_e_id(self, rr_e_id: int) -> [Rr]:
        return self.rr_dao.get_all_requests_by_e_id(rr_e_id)

    def create_request(self, rr: Rr) -> Rr:
        return self.rr_dao.create_request(rr)

    def get_all_requests(self) -> [Rr]:
        return self.rr_dao.get_all_requests()

    def update_request(self, rr_id, rr_status: str) -> Rr:
        rr = self.rr_dao.get_request_by_rr_id(rr_id)
        return self.rr_dao.update_request(rr, rr_status)

    def get_reports_by_statuses(self, statuses: str) -> dict:
        return self.rr_dao.get_reports_by_statuses(statuses)

    def get_reports_for_all(self) -> dict:
        return  self.rr_dao.get_reports_for_all()

    def get_reports_for_employee(self) -> [dict]:
        return self.rr_dao.get_reports_for_employee()