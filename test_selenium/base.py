import os

from selenium import webdriver

class Base():
    def setup(self):
        """
        多浏览器处理
        :return:
        """
        # browser = os.getenv("browser")
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        # elif browser == 'headless':
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()

        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)    # 复用浏览器
        self.driver = webdriver.Chrome()
        # self.vars = {}
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()