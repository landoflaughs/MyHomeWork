from appium.webdriver.common.mobileby import MobileBy

from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.editPersonInfo_page import EditPersonInfoPage


class PersonInfo(BasePage):
    def editPersonInfo(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return EditPersonInfoPage(self.driver)