from selenium.webdriver import Keys

from ui.BasePage import BasePage
from ui.Locators import Locators


class MainPage(BasePage):
    def search(self, query):
        el = self.wait(*Locators.search_main)
        el.clear()
        el.send_keys(query, Keys.ENTER)

        self.wait_search()

    def wait_search(self):
        self.wait_path('search')
