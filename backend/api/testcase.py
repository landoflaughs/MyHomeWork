# restful 插件支持把get和post定义为类
# 定义用例接口
from flask import request
from flask_restful import Resource

from backend.api.verify_token import auth
from backend.backend_server import db, api
from backend.date_base.testcase_table import TestCase


class TestCaseAdd(Resource):
    # method_decorators装饰器不声明类型，默认对所有请求都适用 get post ...
    # 加入装饰器，使得用例获取也要校验
    method_decorators = [auth.login_required]
    def post(self):
        """
        新增用例,这里用接口创建，后面讲用例解析的方式创建
        把请求体的数据发送到数据库
        :return:
        """
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg": "ok"}


class TestCaseGet(Resource):
    # get 方法代表接受get请求
    method_decorators = [auth.login_required]
    def get(self):
        """
        获取所有的测试用例数据
        1. 查找所有用例
        2、 格式化为字典
        :return:
        """
        test_cases = TestCase.query.all()
        format_test_cases = [i.as_dict() for i in test_cases]
        return {"msg": 'ok', "data": format_test_cases}
        # 如果url中存在option参数为del_testcase 代表要删除用例


class TestCaseDelete(Resource):
    # get 方法代表接受get请求
    method_decorators = [auth.login_required]
    def get(self):
        """
        获取所有的测试用例数据
        1. 查找所有用例
        2、 格式化为字典
        :return:
        """
        if "nodeid" in request.args:
            # 利用nodeid 参数指明要删除的用例
            nodeid = request.args.get("nodeid")
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
            db.session.commit()
            return {"msg": "deleted!"}
        elif "nodeids" in request.args:
            nodeids = request.args.get("nodeids")
            for nodeid in nodeids.split(","):
                # 查询此用例后，进行删除
                testcase = TestCase.query.filter_by(nodeid=nodeid)
                db.session.delete(testcase)
            db.session.commit()


class TestCaseUpdate(Resource):
    """
    更新测试用例
    """
    method_decorators = [auth.login_required]
    def post(self):
        request_body = request.json
        testcase = TestCase.query.filter_by(nodeid=request_body.get("nodeid")).first()
        testcase.description = request_body.get("description")
        db.session.commit()
        return {"msg": "updated!"}
