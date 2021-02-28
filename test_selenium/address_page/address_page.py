from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            '''
            判断是否进入了添加成员页面，没有则继续按添加成员按钮
            :param driver:
            :return:
            '''
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            print(eles)
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