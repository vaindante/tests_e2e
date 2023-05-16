import pytest
from faker import Faker

from api import Api
from config_test import config
from ui.Application import Application


@pytest.fixture(scope='session')
def app():
    _app = Application('https://food.ru/')

    yield _app

    _app.close()


@pytest.fixture
def api():
    with Api(config.url) as api:
        yield api


@pytest.fixture(scope='session')
def faker():
    return Faker('ru_RU')
