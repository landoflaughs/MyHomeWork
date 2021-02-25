import json
from time import sleep

import selenium
from selenium import webdriver

# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.base import Base


class TestChromeLoginTmp(Base):
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com/')
    #     self.driver.implicitly_wait(5)
    #
    # def teardown(self):
    #     self.driver.quit()
    #
    # def test_baidu(self):
    #
    #     self.driver.find_element(By.ID, 'kw').send_keys('霍格沃兹测试学院')
    #
    #     self.driver.find_element(By.ID, 'su').click()
    #
    #     self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院 - 主页').click()
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://ceshiren.com/')
    #     self.driver.implicitly_wait(3)

    # def test_wait(self):
    #     self.driver.find_element(By.XPATH, '//*[@title="原创精华文章,有100元奖金"]').click()
    #     # def wait(x):
    #     #     return len(self.driver.find_elements(By.XPATH, '//*[@class="d-button-label"]')) >= 1
    #     # WebDriverWait(self.driver, 10).until(wait)
    #     WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="d'
    #                                                                                                 '-button-label"]')))
    #     self.driver.find_element(By.XPATH, '//*[@title="有了新帖的活动主题"]').click()

    # def test_main_tmp(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
    #     self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()

    def test_login_tmp(self):
        """
        基于浏览器复用后的内容进行操作
        - cmd中输入 chrome -remote-debugging-port=9222
        - 然后执行python代码
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()


    def test_cookie_tmp(self):
        """
        利用 cookie 进行登陆
        :return:
        """
        # 获取cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("cookies_tmp.txt", "w", encoding='utf-8') as f:
        #     json.dump(cookies, f)

        # 读取cookies
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        with open("cookies_tmp.txt", "r", encoding='utf-8') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(5)