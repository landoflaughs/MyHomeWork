import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from test_selenium.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com/')


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_ActionChains.py'])