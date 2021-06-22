from abc import ABC, abstractmethod
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr


class RrService(ABC):

    @abstractmethod
    def get_all_requests_by_e_id(self, rr_e_id: int) -> [Rr]:
        pass

    @abstractmethod
    def create_request(self, rr: Rr) -> Rr:
        pass

    @abstractmethod
    def get_all_requests(self) -> [Rr]:
        pass

    @abstractmethod
    def update_request(self, rr_id: int, rr_status: str) -> Rr:
        pass

    @abstractmethod
    def get_reports_by_statuses(self, statuses: tuple) -> dict:
        pass

    @abstractmethod
    def get_reports_for_all(self) -> dict:
        pass

    @abstractmethod
    def get_reports_for_employee(self) -> [dict]:
        pass
