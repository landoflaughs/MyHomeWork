import time

from test_selenium.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script('return document.getElementById("su")')  # 若想返回，则加return
        element.click()
        time.sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        time.sleep(3)
        for code in [
            'document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))  # 对代码块里的数据打印出来，以便分析
