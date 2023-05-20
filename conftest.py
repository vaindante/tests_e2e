import pytest

from api.api import ClientApi
from ui.Application import Application


@pytest.fixture(scope='session')
def app():
    _app = Application('https://food.ru/')

    yield _app

    _app.close()


@pytest.fixture(scope='session')
def api():
    _api = ClientApi()
    yield _api

    _api.session.close()
