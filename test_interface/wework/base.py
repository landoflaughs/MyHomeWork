import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww818d7a4f0e100712",
                  "corpsecret": "rP8jaJlLBsWAXZbNK28c8DN7YAXW8GfKahEGywBKOGE"}
        r = self.s.get(url, params=params)
        return r.json()['access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
