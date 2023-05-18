from time import sleep

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def wd():
    wd = Chrome(service=Service(ChromeDriverManager().install()))
    wd.get('https://food.ru')

    sleep(.5)

    yield wd

    wd.close()

