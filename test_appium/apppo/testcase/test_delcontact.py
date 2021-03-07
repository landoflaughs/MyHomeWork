from test_appium.apppo.page.app import App


class TestDelContact:

    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        # self.app.stop()
        pass

    def test_delContact(self):
        name = 'test_3'
        deletepage1 = self.main.goto_addressList().click_search()   # 进入搜索界面
        deletepage1.searchOneName(name) # 搜索
        deletepage2 = deletepage1.verifyNameFound(name).clickThreeDot().editPersonInfo()    # 进入编辑个人信息界面
        deletepage2.deletePersonInfo()  # 删除个人信息
        deletepage2.confirmDelete().verifyDeleteSuccess(name)   # 确认指定信息已经被删除