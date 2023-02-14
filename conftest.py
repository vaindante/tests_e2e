import pytest
from faker import Faker

from api import Api
from config_test import config


@pytest.fixture
def api():
    with Api(config.url) as api:
        yield api


@pytest.fixture(scope='session')
def faker():
    return Faker('ru_RU')
