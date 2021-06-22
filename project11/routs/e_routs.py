from flask import Flask, jsonify, request
from flask_cors import CORS

from daos.e_daos.e_daos import EDao
from daos.e_daos.e_daos_postgres import EDaoPostgres
from exceptions.u_p_exception import UsernamePasswordNotMatch
from services.e_services.e_service import EService
from services.e_services.e_service_impl import EServiceImpl

e_dao: EDao = EDaoPostgres()
e_service: EService = EServiceImpl(e_dao)


def e_create_rout(app: Flask):
    CORS(app)

    @app.route('/logging/username/<username>/password/<password>', methods=['GET'])
    def logging(username: str, password: str):

        try:
            data = e_service.check_login_e_m(username, password)
            app.logger.info(f' logging was done successfully ')
            return jsonify(data.serialized()), 200
        except UsernamePasswordNotMatch as e:
            return str(e), 400

