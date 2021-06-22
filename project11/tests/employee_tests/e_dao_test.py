from daos.e_daos.e_daos import EDao
from daos.e_daos.e_daos_postgres import EDaoPostgres
from exceptions.u_p_exception import UsernamePasswordNotMatch
from entities.employees import Employee
from entities.manager import Manager
from entities.r_request import Rr

e_dao: EDao = EDaoPostgres()


class TestEDao:

    def test_check_login_e_m(self) -> Employee or Manager:
        try:
            e_dao.check_login_e_m(" ", " ")
            assert False
        except UsernamePasswordNotMatch as e:
            str(e)

    def test_check_login_e_m_1(self) -> Employee or Manager:
        try:
            e_dao.check_login_e_m("abcd", " ")
            assert False
        except UsernamePasswordNotMatch as e:
            str(e)

    def test_check_login_e_m_2(self) -> Employee or Manager:
        obj=e_dao.check_login_e_m("abc", '123')
        assert type(obj)==Employee

    def test_check_login_e_m_3(self) -> Employee or Manager:
        obj = e_dao.check_login_e_m("abc", 'xyz')
        assert type(obj) == Manager