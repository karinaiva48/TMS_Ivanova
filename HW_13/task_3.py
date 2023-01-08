"""
3. Создайте класс Validator который позволяет проводить проверку данных пользователя при
регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — от 6 до 10 символов английского алфавит и цифр 0-9 в любой последовательности
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Проверку на соответствие правилам выполнить регулярными выражениями. По результатам работы метода validate пользователь получит True если все 3 элемента прошли проверку, в противном случае - False
"""


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
        if re.match(r'^[\w.-]+@[\w.-]+\.(\S{2}$)', self.email):
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


validator = Validator('Karina48', 'Lswfgi#17', 'karinaiva@gmail.by')
validator.validation()


validator_1 = Validator('Karin', 'Lswfgi#17', 'karinaiva@gmail.com')
validator_1.validation()