from pprint import pprint
from time import sleep

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main(wd):
    wd.get('https://food.ru')
    sleep(.5)

    el = wd.find_element(By.XPATH, "//input[contains(@class, 'searchInput')]")
    el.send_keys('солянка', Keys.ENTER)

    sleep(2)

    els = wd.find_elements(
        By.XPATH,
        "//div[contains(@class, 'card_contentWrapper')]//div[contains(@class, 'card_title_')]")

    pprint([
        el.text for el in els
    ])


if __name__ == '__main__':
    wd = None
    try:
        wd = Chrome(service=Service(ChromeDriverManager().install()))
        main(wd)
    finally:
        if wd is not None:
            wd.close()
