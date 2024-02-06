import pytest


@pytest.fixture(scope='function')
def url():
    URL = "https://reqres.in"
    return URL
