import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
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
        pass
        # self.driver.quit()

    def test_search(self):
        '''
        1. 打开雪球app
        2. 点击搜索输入框
        3. 向搜索输入框里面输入 alibaba
        4. 在搜索结果里面学则 阿里巴巴 然后进行点击
        5. 获取这只香港阿里巴巴的股价 并判断这只股价的价格>200
        :return:
        '''
        print("搜索测试用例")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)   # by_id也能用
        assert current_price > 200
        # 不要用class.textview进行定位

    def test_attr(self):
        '''
        1. 打开雪球应用首页
        2. 定位首页的搜索框
        3、 判断搜索框是否可用，并查看搜索框name属性值
        4. 打印搜索框这个元素的左上角坐标和它的宽高
        5. 向搜索框输入 alibaba
        6. 判断阿里巴巴是否可见
        7. 如果可见，打印搜索成功，点击，如果不可见，打印搜索失败
        :return:
        '''
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.size)
        print(element.location)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            element_displayed = alibaba_element.get_attribute('displayed')
            if element_displayed == 'true':
                print('搜索成功')
            else:
                print('搜索失败')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()   #获取宽高
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_myinfo(self):
        '''
        1. 点击我的， 进入个人信息页面
        2. 点击登录 进入到登录页面
        3. 输入用户名 输入密码
        4. 点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('12345')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('12345')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        '''
        滚动定位
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).scrollIntoView(new UiSelector().text("我的").instance(0));')


if __name__ == '__main__':
    pytest.main()
