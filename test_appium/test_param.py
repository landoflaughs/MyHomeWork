import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'  # true: 首次启动时不停止app
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'  # 输入中文
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(7)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()
        pass



    @pytest.mark.parametrize('searchkey,type,expect_price', [
        ('alibaba', 'BABA', 220),
        ('xiaomi', '01810', 24)
    ])
    def test_search(self, searchkey, type, expect_price):
        '''
        1、打开雪球应用
        2、点击搜索框
        3、输入搜索词 ‘alibaba’ ‘xiaomi’
        4、点击第一个搜索结果
        5、判断股票价格
        :return:
        '''

        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        price_element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*["
                                                                 "@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(price_element.text)
        print(current_price)
        # expect_price = 230
        assert_that(current_price, close_to(expect_price, expect_price*0.1))