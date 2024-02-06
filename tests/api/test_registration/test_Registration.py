from python.api.register.api import Register
from python.api.register.models import RegisterUser
from schemas.registration import valid_schema, invalid_schema
from tests.api.configuration.conftest import url


class TestRegistrationApi:
    def test_successful_registration_api(self, url):
        body = RegisterUser.random()
        response = Register(url).register_user(body=body, schema=valid_schema)
        assert response.status == 200
        assert response.response.get('id') == 4
        assert response.response.get('token') == "QpwL5tke4Pnpja7X4"
        return response

    def test_unsuccessful_registration_api(self, url):
        body = RegisterUser.random_email()
        response = Register(url).register_user(body=body, schema=invalid_schema)
        assert response.status == 400
        assert response.response.get('error') == 'Missing password'
        return response
