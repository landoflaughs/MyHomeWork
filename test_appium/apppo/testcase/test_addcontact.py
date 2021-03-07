from test_appium.apppo.page.app import App


class TestAddContact:

    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        self.app.stop()

    def test_addContact(self):
        name = 'test_3'
        phonenum = 10000000003
        editpage = self.main.goto_addressList().click_addcontact().addcontact_manual()
        editpage.edit_contact(name,phonenum)
        editpage.verify_ok()
