from python.api.register.api import Login
from python.api.register.models import LoginUser
from schemas.registration import valid_schema
from tests.api.configuration.conftest import url


class TestLoginApi:
    def test_successful_login_api(self, url):
        body = LoginUser.successful()
        response = Login(url).login_user(body=body, schema=valid_schema)
        assert response.status == 200
        assert response.response.get('token') == "QpwL5tke4Pnpja7X4"
        return response

    def test_unsuccessful_login_api(self, url):
        body = LoginUser.unsuccessful()
        response = Login(url).login_user(body=body, schema=valid_schema)
        assert response.status == 400
        assert response.response.get('error') == 'Missing password'
        return response
