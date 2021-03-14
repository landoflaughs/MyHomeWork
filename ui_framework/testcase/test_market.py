from ui_framework.page.app import App


class TestMarket:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        # self.app.stop()
        pass

    def test_goto_market(self):
        self.main.goto_market()