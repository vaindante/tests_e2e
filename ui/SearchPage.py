from ui.BasePage import BasePage
from ui.Locators import Locators


class SearchPage(BasePage):
    def search(self, query):
        el = self.wait(*Locators.search_filters)
        el.clear()
        el.send_keys(query)

    def get_recipe_titles(self):
        els = self.find_elements(*Locators.recipe_title)
        return [
            el.text.strip() for el in els
        ]

    def add_filter(self, name):
        self.wait(*Locators.filter(name)).click()

    def get_recipe_type(self):
        els = self.find_elements(*Locators.recipe_type)
        return [
            el.text.strip() for el in els
        ]
