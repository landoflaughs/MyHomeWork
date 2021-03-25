# -*-coding:GBK -*-

import json

import requests

class TestAddress:
    def setup(self):
        self.token = self.get_token()


    def get_token(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww818d7a4f0e100712&corpsecret=rP8jaJlLBsWAXZbNK28c8DN7YAXW8GfKahEGywBKOGE')
        return r.json()['access_token']

    def test_get_information(self):
        user_id = '1'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}')
        print(r.json())


    def test_create_member(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "kenan",
            "name": "柯南",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1]
        }

        r = requests.post(url, json=data)
        print(r.json())

    def test_delete_member(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=kenan'
        r = requests.get(delete_url)
        print(r.json())

    def test_defect_member(self):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=kenan'
        r = requests.get(get_member_url)
        print(r.json())
        assert "柯南" == r.json()['name']

    def test_update_member(self):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "kenan",
            "name": "柯南",
            "mobile": "13800009999",
        }
        r = requests.post(url=update_member_url, json=data)
        print(r.json())