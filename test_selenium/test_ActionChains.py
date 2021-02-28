import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get('')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.click(element_doubleclick)
        action.click(element_rightclick)
        action.perform()

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_ActionChains.py'])