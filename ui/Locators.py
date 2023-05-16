from selenium.webdriver.common.by import By


class Locators:
    search_main = By.XPATH, "//input[contains(@class, 'searchInput')]"
    search_filters = By.XPATH, "//input[contains(@class, 'filters_input')]"
    recipe_title = By.XPATH, "//div[contains(@class, 'card_contentWrapper')]//div[contains(@class, 'card_title_')]"
    recipe_type = By.XPATH, "//div[contains(@class, 'card_contentWrapper')]//div[contains(@class, 'card_badge')]"
    button = By.XPATH, "//button[contains(@class, 'searchInput')]"

    @staticmethod
    def filter(name):
        return By.XPATH, \
               f"//button[contains(@class, 'filters_filter') and contains(text(), '{name}')]"
