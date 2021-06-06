from flask import g
from flask_restful import Resource

from backend.api.verify_token import auth


# 为什么集成resource才能实现登录，因为继承的flask restful
class Login(Resource):
    # auth.login_required 是 httpAuth的用法，添加了此装饰器的对象会回调校验方法
    # method_decorators代表给Login接口添加一个装饰器，这是flask restful的写法
    method_decorators = {'get': [auth.login_required]}

    def get(self):
        # 使用verify password中 校验成功后的用户信息
        # 由于g.user里包括user的所有信息包括方法，所以这里生成token用g
        token = g.user.generate_auth_token()
        return {"access_token": token}
