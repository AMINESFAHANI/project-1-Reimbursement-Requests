from flask import Flask, request, jsonify
import logging

from flask_cors import CORS

from entities.employees import Employee
from routs.e_routs import e_create_rout
from routs.rr_routs import rr_create_rout

app: Flask = Flask(__name__)

CORS(app)


@app.get("/hello")
def hello():
    employee = Employee(33, "amin", "123", "ooo")
    return jsonify(employee.serialized()), 202
    # return "hello"


logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
e_create_rout(app)
rr_create_rout(app)

if __name__ == '__main__':
    app.run()
