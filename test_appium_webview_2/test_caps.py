import pytest
from appium import webdriver
from hamcrest import *


class TestGetAttr():
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

        # http://appium.io/docs/en/writing-running-appium/caps/index.html  查看参数的用法
        desired_caps['newCommandTimeout'] = 300
        desired_caps['udid'] = 'emulator-5554'
        desired_caps['autoGrantPermissions'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(7)

    def teardown(self):
        pass
