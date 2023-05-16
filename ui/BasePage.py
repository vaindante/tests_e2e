from dataclasses import dataclass
from typing import List, Any

import allure
from furl import furl
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class BasePage:
    wd: 'WebDriver'
    app: 'Any'

    @allure.step('Поиск элемента')
    def find_element(self, locator) -> 'WebElement':
        return self.wd.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, *locator) -> List[WebElement]:
        return WebDriverWait(self.wd, 120).until(
            ec.visibility_of_all_elements_located(locator),
            message='Не дождались отображения элементов'
        )

    @allure.step('Поиск элемента')
    def wait(self, *locator) -> 'WebElement':
        return WebDriverWait(self.wd, 120).until(
            ec.visibility_of_element_located(locator),
            message='Не дождались отображения элемента'
        )

    def wait_path(self, path):
        WebDriverWait(self.wd, 20).until(
            ec.url_contains((self.app.base_url / path).url)
        )

    @allure.step('Клик по элементу')
    def click(self, *locator):
        self.wait(locator).click()

    @allure.step('Открытие страницы')
    def open(self, path):
        if furl(path).scheme:
            url = furl(path)
        else:
            url = self.app.base_url / path

        self.wd.get(url.url)
