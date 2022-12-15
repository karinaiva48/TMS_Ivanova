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

class InvalidLogin(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidEmail(Exception):
    pass

class Validation(Exception):
    pass

class Validator:
    """
    Класс принимает логин,пароль,email и делает валидацию этих аргументов
    """

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def validate_email(self):
        """
        Метод делает валидацию на проверку email
        """
        if re.match(r'^[\w.-]+@[\w.-]+\.(\S{2}$)', self.email):
            return True
        else:
            raise InvalidEmail

    def validate_login(self):
        """
        Метод делает валидацию на проверку логина
        """
        if re.match(r'[0-9a-zA-Z]{6,10}$', self.login):
            return True
        else:
            raise InvalidLogin

    def validate_password(self):
        """
        Метод делает валидацию на проверку пароля
        """
        if not re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[$%#^])[0-9a-zA-Z$%#^]{8,}$', self.password):
            raise InvalidPassword
        else:
            return True

    def validation(self):
        """
        Метод принимает другие методы и если в них случаются ошибки обрабатывает их и выводит собственную ошибку
        """
        try:
            self.validate_email()
            self.validate_login()
            self.validate_password()
        except InvalidLogin:
            raise Validation
        except InvalidEmail:
            raise Validation
        except InvalidPassword:
            raise Validation


validator = Validator("Sasha1f", "#sashaShro#", "sobaka@mail.by")
validator.validation()