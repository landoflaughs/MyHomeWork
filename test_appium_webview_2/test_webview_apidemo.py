from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName' : 'Android',
            'platformVersion' : '6.0',
            'appPackage' : 'io.appium.android.apis',
            'appActivity' : 'io.appium.android.apis.ApiDemos',
            # 'browserName' : 'Browser',
            # 'noReset' : True,
            'deviceName' : 'emulator-5554',
            'chromedriverExecutable' : 'E:/googledriver/2.24/chromedriver.exe'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        '''
        webview的两种定位方式
        1、使用选然后的页面，用accessibility_id 定位  这种方法不稳定
        2、切换上下文后,对web组件进行操作
        :return:
        '''

        # self.driver.get('http://m.baidu.com')
        # sleep(5)
        self.driver.find_element_by_accessibility_id("Views").click()   # accessibility id 即 content-desc
        print(self.driver.contexts)
        webview = 'WebView'
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0))'
                                 f'scrollIntoView(new UiSelector().text("{webview}").instance(0));').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'I has no focus').send_keys('this is a test string')

        print(self.driver.contexts)
        self.driver.switch_to_context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, 'i am a text box').send_keys('this is a test string')