from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 生成具有时间维护功能的token
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from datetime import datetime

from backend.backend_server import app, db



class User(db.Model):
    # 以下字段代表数据库中的表头
    # db.Integer 是整型，primary_key 代表主键，唯一标识一条数据，是一条数据的身份证
    id = db.Column(db.Integer, primary_key=True)
    # db.String（80） 代表 80 个字符的字符串
    # unique 代表是不是唯一
    # nullable 是否可为空，如果为 False ，说明为必填项
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    time = db.Column(db.Time(), unique=False, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def generate_auth_token(self, expires_in=600000):
        """
        生成token
        :param expires_in:
        :return:
        """
        # expires_in 代表超时时间
        # app.config['SECRET_KEY']: token种子用于生成token，值随机无要求
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'], expires_in=expires_in)
        token_id = self.username + self.password + str(datetime.now())
        token = serializer.dumps({'id': self.id, 'token_id': token_id}).decode()    # serializer生成的token是字节，用decode
        # 转化为字符串,字符串才可以转为json格式， login中的return才会正常转为json，而不会报错
        return token
        # dumps 反序列化 把一个python对象(字典)转化为字符串，通过反序列化把一组数据转化生成token

    # 方便外界进行调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls, token):
        """
        校验token
        :param token:
        :return:None or User
        """
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'])
        # loads用于序列化，把Token转成Python对象(字典)
        try:
            token_loads_result = serializer.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        # 利用id查找到user表中的一个字段
        return User.query.get(token_loads_result['id'])


if __name__ == "__main__":
    ## 删库
    # db.drop_all()
    ## 在远程数据库中创建表
    # db.create_all()
    pass
