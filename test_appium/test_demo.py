from time import sleep

import pytest
from appium.webdriver.common.mobileby import MobileBy

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWechat():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'  # true: 首次启动时不停止app
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'  # 输入中文
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 1    # 控制每一步的等待时间
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)    # 模拟器企业微信打开较慢
        self.driver.implicitly_wait(7)

    def teardown(self):
        # pass
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='通讯录']").click()
        # uiautomator实现滑动查找 一定要 外面单引号 里面双引号
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//android.widget.RelativeLayout//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/b7m").send_keys('星期六')
        self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys('13131377666')
        self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()

        locator = (By.ID, "com.tencent.wework:id/ig0")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element_by_id("com.tencent.wework:id/ig0").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='星期六']")
