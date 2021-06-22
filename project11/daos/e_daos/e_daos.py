from abc import ABC, abstractmethod
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr


class EDao(ABC):

    @abstractmethod
    def check_login_e_m(self, username: str, password: str) -> Employee or Manager:
        pass


