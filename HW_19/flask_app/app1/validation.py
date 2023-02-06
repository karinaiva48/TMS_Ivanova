import re

class InputLogin(Exception):
    pass

class InputPassword(Exception):
    pass

class InputEmail(Exception):
    pass

class Validation(Exception):
    pass

class Validator:

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def validate_login(self):
        if re.match(r'[0-9a-zA-Z]{6,10}$', self.login):
            return True
        else:
            raise InputLogin

    def validate_password(self):
        if re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[$%#^])[0-9a-zA-Z$%#^]{8,}$', self.password):
            return True
        else:
            raise InputPassword

    def validate_email(self):
        if re.match(r'^[\w.-]+@[\w.-]+\.[a-z]{2,3}', self.email):
            return True
        else:
            raise InputEmail

    def validation(self):
        try:
            self.validate_email()
            self.validate_login()
            self.validate_password()
        except InputLogin:
            raise Validation
        except InputEmail:
            raise Validation
        except InputPassword:
            raise Validation
        return True

