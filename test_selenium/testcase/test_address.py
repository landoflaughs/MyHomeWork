from test_selenium.address_page.main_page import MainPage


class TestAddress:
    def test_address(self):
        main = MainPage()
        main.goto_address().add_member()