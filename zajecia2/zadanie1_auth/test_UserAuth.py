from subprocess import check_output
from unittest import TestCase

from zajecia2.zadanie1_auth.UserAuth import UserAuth


class TestUserAuth(TestCase):
    def test_login_success(self):
        auth = UserAuth({"admin": "1234", "user": "abcd"})
        result = auth.login("admin", "1234") # Sukces
        self.assertTrue(result)

    def test_login_incorrect_password(self):
        auth = UserAuth({"admin": "1234", "user": "abcd"})
        result = auth.login("user", "wrongpass") # Powinien rzucić WrongPasswordError
        self.assertFalse(result)

    def test_login_incorrect_username(self):
        auth = UserAuth({"admin": "1234", "user": "abcd"})
        result = auth.login("unknown", "pass") # Powinien rzucić UserNotFoundError
        self.assertFalse(result)
