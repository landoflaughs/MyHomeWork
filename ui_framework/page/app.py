
# 启动 停止 重启app
import yaml
from appium import webdriver

from ui_framework.page.basepage import BasePage
from ui_framework.page.main_page import MainPage

with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires = datas["desirecaps"]
    ip = datas['server']["ip"]
    port = datas['server']["port"]

class App(BasePage):
    def start(self):
        if self.driver == None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()


    def goto_main(self):
        return MainPage(self.driver)

