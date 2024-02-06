from faker import Faker

fake = Faker()


class RegisterUser:
    @staticmethod
    def random():
        # email = fake.email()
        # password = fake.password()
        email = "eve.holt@reqres.in"
        password = "pistol"
        return {"email": email, "password": password}

    @staticmethod
    def random_email():
        email = fake.email()
        return {"email": email}


class LoginUser:
    @staticmethod
    def successful():
        email = "eve.holt@reqres.in"
        password = "cityslicka"
        return {"email": email, "password": password}

    @staticmethod
    def unsuccessful():
        email = fake.email()
        return {"email": email}


class CRUD_User:
    @staticmethod
    def get_user_create():
        name = "morpheus"
        job = "leader"
        return {"name": name, "job": job}

    @staticmethod
    def get_user_update():
        name = "morpheus"
        job = "zion resident"
        return {"name": name, "job": job}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
