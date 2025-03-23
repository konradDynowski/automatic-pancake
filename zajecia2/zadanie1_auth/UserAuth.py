from zajecia2.zadanie1_auth.UserNotFoundError import UserNotFoundError
from zajecia2.zadanie1_auth.WrongPasswordError import WrongPasswordError


class UserAuth:
    def __init__(self, users=None):
        if users:
            self.users = users
        else:
            self.users = dict({})

    def login(self, username, password):
        try:
            if username in self.users.keys():
                if password == self.users[username]:
                    return True
                else:
                    raise WrongPasswordError()
            else:
                raise UserNotFoundError()
        except UserNotFoundError:
            print("user not found")
            return False

        except WrongPasswordError:
            print("incorrect password")
            return False
