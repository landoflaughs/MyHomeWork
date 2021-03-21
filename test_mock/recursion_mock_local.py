import json
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx, http
from datetime import datetime

class HS:

    def request(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open(r"D:\PyCharmWork\MyHomeWork\test_mock\xueqiu_stock.json", encoding="utf-8") as f:
                data = self.handle_data(json.loads(f.read()))

                flow.response = http.HTTPResponse.make(200,  # (optional) status code

                                                       json.dumps(data),  # (optional) content
                                                       {"Content-Type": "text/html"}  # (optional) headers
                                                       )


    def response(self, flow: http.HTTPFlow):
        pass

    def handle_data(self, data):
        """
        :param data: 传入的数据信息
        :return: 递归过后的数据信息
        """
        # 1. 罗列各种情况 2. 针对不同的数据结构做不同的数据处理
        if isinstance(data, dict):
            #  如果是dict 就继续遍历 对应的value
            for key, value in data.items():
                data[key] = self.handle_data(value)

        elif isinstance(data, datetime):
            data = data
        elif isinstance(data, list):
            #递归算法，如果是list 就继续遍历列表中的元素
            # data_new = []
            # for item in data:
            #     data_new.append(handle_data(item))
            # 把 原本的遍历操作使用列表推导式表达出来
            data = [self.handle_data(item) for item in data]
        elif isinstance(data, str):
            #    如果是str， 做+ "a"操作
            #
           # if "-" in data:
           #     pass
            data = data
            if data == '招商银行':
                data = 'hogwartzzzz'
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, (int, float)):
            # 如果是整型或者float，做倍增
            data = data*1.5
            if  data < 0:
                data = data * -1
        else:
            # 如果是其他数据类型，保持原样
            data = data
        return data


# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    HS()
]
