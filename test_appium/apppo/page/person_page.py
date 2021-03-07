from appium.webdriver.common.mobileby import MobileBy

from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.personinfo_page import PersonInfo


class PersonPage(BasePage):
    def clickThreeDot(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/iga")
        return PersonInfo(self.driver)