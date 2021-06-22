from abc import ABC, abstractmethod
from entities.employees import Employee
from entities.manager import Manager


class EService(ABC):

    @abstractmethod
    def check_login_e_m(self, username: str, password: str) -> Employee or Manager:
        pass