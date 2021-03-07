from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.apppo.page.base_page import BasePage


class SearchNamePage2(BasePage):
    def verifyDeleteSuccess(self, name):
        sleep(2)
        elelist_after_delete = self.finds(MobileBy.XPATH, f"//*[@text='{name}']")
        if len(elelist_after_delete) == 1:
            print('delete success')
        else:
            print('delete fail')