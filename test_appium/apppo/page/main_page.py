from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.apppo.page.addresslist_page import AddressListPage
from test_appium.apppo.page.base_page import BasePage


class MainPage(BasePage):
    addressList_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addressList(self):
        # click contact
        self.find(*self.addressList_element).click()   # 解元组
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return AddressListPage(self.driver)