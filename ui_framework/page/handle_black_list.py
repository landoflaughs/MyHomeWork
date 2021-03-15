import allure
from appium.webdriver.common.mobileby import MobileBy
from ui_framework.page.logger import log
import allure


def handle_black_list(func):
    black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']

    def run(*args, **kwargs):
        self = args[0]
        try:
            log.debug("find " + args[2])
            return func(*args, **kwargs)
        except Exception:
            allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)

            for ele_xpath in black_list:
                eles = self.finds(MobileBy.XPATH, ele_xpath)
                if len(eles) > 0:
                    eles[0].click()
                    return func(*args, **kwargs)  # 递归调用

    return run