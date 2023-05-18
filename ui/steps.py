from time import sleep

from selenium.webdriver import Keys

from ui.Locators import Locators


def search(wd, query):
    el = wd.find_element(*Locators.search)
    el.send_keys(query, Keys.ENTER)

    sleep(2)


def get_titles_recipe(wd):
    els = wd.find_elements(*Locators.recipes_title)

    return [
        el.text for el in els
    ]
