from daos.e_daos.e_daos import EDao
from entities.employees import Employee
from entities.manager import Manager
from services.e_services.e_service import EService


class EServiceImpl(EService):

    def __init__(self, e_dao: EDao):
        self.e_dao = e_dao

    def check_login_e_m(self, username: str, password: str) -> Employee or Manager:
        return self.e_dao.check_login_e_m(username, password)

