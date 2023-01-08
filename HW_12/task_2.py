"""
2) Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, validate_password)
в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), при соответствии — возвращается значение True.
 В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия — вызвать ошибку ValidationError.
"""
import string
from string import ascii_lowercase, ascii_uppercase, punctuation

class InvalidLogin(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidEmail(Exception):
    pass

class ValidationError(Exception):
    pass

class Validator():
    
    @staticmethod
    def validate(user_data: tuple) -> bool:
        try:
            Validator.validate_login(user_data[0])
            Validator.validate_password(user_data[1])
            Validator.validate_email(user_data[2])
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError
        else:
            return True

    @staticmethod
    def validate_login(login: str) -> bool:
        if len(login) > 6:
            return True
        else:
            raise InvalidLogin
    
    @staticmethod
    def validate_password(password: str) -> bool:
        if (len(password) > 8 and 
            len([x for x in password if x in string.ascii_uppercase]) > 0 and
            len([x for x in password if x in string.ascii_lowercase]) > 0 and
            len([x for x in password if x in string.punctuation]) > 0):
           return True
        else:
            raise InvalidPassword
        
    @staticmethod
    def validate_email(email: str) -> bool:
        if '@' in email and email[-3] == '.' and email[-3:].isalpha():
            return True
        else:
            raise InvalidEmail


Validator.validate(('karinaiva48', 'Karina#97', 'karinaiva@gmail.com'))