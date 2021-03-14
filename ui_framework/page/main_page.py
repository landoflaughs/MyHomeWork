from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find(By.XPATH ,'//*[@text="行情"]').click()
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")