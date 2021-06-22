from flask import Flask, jsonify, request
from flask_cors import CORS

from daos.e_daos.e_daos import EDao
from daos.e_daos.e_daos_postgres import EDaoPostgres
from daos.r_request_daos.rr_dao import RrDao
from daos.r_request_daos.rr_postgres_dao import RrDaoPostgres
from entities.r_request import Rr
from exceptions.ResourceNotFoundError import ResourceNotFoundError
from exceptions.u_p_exception import UsernamePasswordNotMatch
from exceptions.value_type_error import TypeValueError
from services.e_services.e_service import EService
from services.e_services.e_service_impl import EServiceImpl
from services.rr_services.rr_service import RrService
from services.rr_services.rr_sevice_impl import RrServiceImpl

rr_dao: RrDao = RrDaoPostgres()
rr_service: RrService = RrServiceImpl(rr_dao)


def rr_create_rout(app: Flask):
    CORS(app)

    @app.route("/requests/<rr_e_id>", methods=["GET"])
    def get_all_requests_by_e_id(rr_e_id: str):
        try:
            if not rr_e_id.isnumeric():
                raise TypeValueError
            requests = rr_service.get_all_requests_by_e_id(int(rr_e_id))
            app.logger.info(f' Get all requests with rr_e_id: {rr_e_id}')
            return jsonify([rr.serialized() for rr in requests]), 200
        except TypeValueError as e:
            return str(e), 404
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route('/requests', methods=['POST'])
    def post_requests():
        try:
            rr = Rr.deserialized(request.json)
            str(rr)
            rr_service.create_request(rr)
            app.logger.info(f'new request registered ID: {rr.rr_id}')
            return jsonify(rr.serialized()), 201
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route("/requests", methods=["GET"])
    def get_all_requests():
        try:
            requests = rr_service.get_all_requests()
            app.logger.info(f' Get all requests')
            return jsonify([rr.serialized() for rr in requests]), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route('/requests/id/<rr_id>/status/<rr_status>', methods=['PATCH'])
    def update_request(rr_id: int, rr_status: str) -> Rr:
        try:
            if not rr_id.isnumeric():
                raise TypeValueError
            rr = rr_service.update_request(int(rr_id), rr_status)
            app.logger.info(f' updated request with rr_id: {rr_id}')
            return jsonify(rr.serialized()), 200
        except TypeValueError as e:
            return str(e), 404
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route("/reports/statuses/<statuses>", methods=["GET"])
    def get_reports(statuses: str):
        try:
            if statuses not in ["rejected", "accepted", "pending"]:
                raise ResourceNotFoundError
            report = rr_service.get_reports_by_statuses(statuses)
            app.logger.info(f' Get report from requests')
            return jsonify(report), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route("/reports", methods=["GET"])
    def get_total_reports():
        try:
            report = rr_service.get_reports_for_all()
            app.logger.info(f' Get report from requests')
            return jsonify(report), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    @app.route("/reports/employee", methods=["GET"])
    def get_reports_employee():
        try:
            reports = rr_service.get_reports_for_employee()
            app.logger.info(f' Get report from employees')
            return jsonify(reports), 200
        except ResourceNotFoundError as e:
            return str(e), 404
