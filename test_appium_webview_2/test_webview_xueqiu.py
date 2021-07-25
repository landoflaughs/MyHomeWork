from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName' : 'Android',
            'platformVersion' : '6.0',
            'appPackage' : 'com.xueqiu.android',
            'appActivity' : 'com.xueqiu.android.common.MainActivity',
            # 'browserName' : 'Browser',
            # 'noReset' : True,
            'deviceName' : 'emulator-5554',
            'chromedriverExecutable' : 'E:/googledriver/2.24/chromedriver.exe'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_browser(self):
        '''

        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
