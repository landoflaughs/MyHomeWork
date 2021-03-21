"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

import mitmproxy
from mitmproxy import ctx,http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
            do the rewrite function
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            print(flow.response.text)
            data = json.loads(flow.response.text)

            data["data"]["items"][0]["quote"]["name"] = 'hogwarts'
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]