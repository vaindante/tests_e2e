import pytest

from ui.Application import Application


@pytest.fixture(scope='session')
def app():
    _app = Application('https://food.ru/')

    yield _app

    _app.close()
