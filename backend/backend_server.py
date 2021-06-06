# -*- coding: gbk -*-
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

host = '192.168.202.128'
user = 'root'
password = 'root'
db = 'ubuntu_test'
charset = 'utf8mb4'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{db}'

db = SQLAlchemy(app)
# ��flaskʵ�����ص�flask-restful
api = Api(app)
app.config["SECRET_KEY"] = "TMP123"

# ȫ�ֵ������ ��ͻ����˶��庯�����ֲ�����
def router():
    from backend.api.login import Login
    from backend.api.testcase import TestCaseAdd, TestCaseUpdate, TestCaseGet, TestCaseDelete
    api.add_resource(Login, '/login')
    api.add_resource(TestCaseAdd, '/testcase/add')
    api.add_resource(TestCaseDelete, '/testcase/delete')
    api.add_resource(TestCaseGet, '/testcase/get')
    api.add_resource(TestCaseUpdate, '/testcase/update')


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # for i in range(5):
    #     data = TestCase(nodeid='nodeid_' + str(i))
    #     db.session.add(data)
    # db.session.commit()
    router()
    app.run(debug=True)
