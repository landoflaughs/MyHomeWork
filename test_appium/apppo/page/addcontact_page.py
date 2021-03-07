# 添加成员
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.apppo.page.base_page import BasePage
from test_appium.apppo.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):

    def addcontact_manual(self):
        # 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)
