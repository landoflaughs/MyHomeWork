from flask import g
from flask_httpauth import HTTPBasicAuth

from backend.date_base.user_table import User

# 初始化auth
auth = HTTPBasicAuth()
"""
通常有个规定
auth 的username 在登录时 是用户名 但在登陆后，是token
"""


@auth.verify_password
def verify_password(username, password):
    # 进行token校验,check token定义为了类方法(@classmethod)，不用实例化User就能调用
    user = User.check_token(username)
    # 如果校验错误或者超时，就认为此时是登录接口
    # 如果校验成功 就认为此时是其他接口,那么就返回一个True就可以了
    # 由于登录接口传进来的是username 和 password 不是token，那么就符合not user
    if not user:
        # 如果是登录接口，那么从数据库中查用户信息，看能否查得到
        user = User.query.filter_by(username=username).first()
        # 如果用户不存在 或者密码不存在 就返回False,可以告诉用户账号或者密码错误
        if not user or user.password != password:
            return False
    # 如果token符合要求 或者用户名密码正确,就把user存起来
    # flask的g代表 flask 的本地线程变量 -> flask线程可共享使用(理解为flask全局变量)
    g.user = user  # g.user里存了user的所有信息 包括数据，和generate token， check token的方法
    return True
