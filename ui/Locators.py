from selenium.webdriver.common.by import By


class Locators:
    search = By.XPATH, "//input[contains(@class, 'searchInput')]"
    recipes_title = By.XPATH, \
                    "//div[contains(@class, 'card_contentWrapper')]//div[contains(@class, 'card_title_')]"
