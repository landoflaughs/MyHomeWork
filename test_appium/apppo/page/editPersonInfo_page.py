from appium.webdriver.common.mobileby import MobileBy

from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.searchname2_page import SearchNamePage2



class EditPersonInfoPage(BasePage):
    def deletePersonInfo(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")

    def confirmDelete(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        return SearchNamePage2(self.driver)

    def cancelDelete(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='取消']")