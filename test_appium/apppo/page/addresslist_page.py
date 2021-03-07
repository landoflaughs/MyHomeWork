from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from test_appium.apppo.page.addcontact_page import AddContactPage
from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.searchname_page import SearchNamePage


class AddressListPage(BasePage):


    def click_addcontact(self):
        element = self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)

    def click_search(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/igk")
        return SearchNamePage(self.driver)

