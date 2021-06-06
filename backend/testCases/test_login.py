import requests

class TestLogin:
    BASE_URL = "http://127.0.0.1:5000"

    def test_login(self):
        r = requests.get(self.BASE_URL + "/login", auth=("xxx","xx"))
        assert r.status_code == 200