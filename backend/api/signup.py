from flask import g, request
from flask_restful import Resource

from backend.api.verify_token import auth


# 为什么集成resource才能实现登录，因为继承的flask restful
from backend.backend_server import db
from backend.date_base.user_table import User


class SignUp(Resource):
    """
    用户注册接口
    """
    def post(self):
        json = request.json
        new_user = User(**json)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return{"msg":"ok", "errcode":200}

