import pytest
from faker import Faker

from api import Api


@pytest.fixture
def api():
    with Api(
            # Base URL for api server
            # 'http://server-for-traning.herokuapp.com/'
    ) as api:
        yield api


@pytest.fixture(scope='session')
def faker():
    return Faker()
