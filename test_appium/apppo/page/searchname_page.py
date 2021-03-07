from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.person_page import PersonPage


class SearchNamePage(BasePage):


    def searchOneName(self,name):
        self.find(MobileBy.XPATH, f"//*[@text='搜索']").send_keys(f'{name}')

    def verifyNameFound(self,name):

        sleep(2)
        elelist = self.finds(MobileBy.XPATH, f"//*[@text='{name}']")
        # list没有.click()等方法
        if len(elelist) > 1:
            elelist[1].click()
            return PersonPage(self.driver)
        else:
            raise NoSuchElementException(f"未找到{name}")