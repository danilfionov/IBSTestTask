from python.api.register.api import Delay
from schemas.registration import valid_schema
from tests.api.configuration.conftest import url


class TestDelayedResponseApi:
    def test_delayed_response_api(self, url):
        response = Delay(url).get_delayed_response(schema=valid_schema)
        assert response.status == 200
        return response
