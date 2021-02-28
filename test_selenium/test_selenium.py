import json
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.base import Base


class TestChromeLoginTmp:
    def test_login_tmp(self):
        """
        基于浏览器复用后的内容进行操作
        - cmd中输入 chrome -remote-debugging-port=9222
        - 然后执行python代码
        :return:
        """
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'        # 加入调试地址
        self.driver = webdriver.Chrome(options=chrome_arg)    # 复用浏览器
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        # 不可交互
        # 1.元素被阻挡，元素前面还有其他不可见元素
        # 2. 元素有多个，需要人工挑选合适的元素
        def wait_name(driver):
            '''
            判断是否进入了添加成员页面，没有则继续按添加成员按钮
            :param driver:
            :return:
            '''
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            eles[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0
            # 对于多元素的查找，有可能会出现找不到元素的情况，在运行之前，手动刷新下页面即可（或自动化）
        # 显示等待
        # 如果显示等待中传入了driver,那么代表隐式等待也会生效
        WebDriverWait(self.driver, 10).until(wait_name)

        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys('星期日')
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys('sunday')
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys('13334534444')
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()


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