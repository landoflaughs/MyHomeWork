from ui_framework.page.basepage import BasePage
from ui_framework.page.search_page import Search


class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.parse("../page/market_page.yaml", "goto_search")
        return Search(self.driver)