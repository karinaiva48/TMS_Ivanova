""" 1. Создать родительский класс Auto, у которого есть атрибуты: brand, age, color, mark и weight.
В классе должны быть реализованы следующие методы — drive, use и stop. Методы drive и stop выводят сообщение «Car <brand> <mark> drives / stops». 
Метод use увеличивает атрибут age на 1 год. Атрибуты brand, age и mark необходимо
инициализировать при объявлении объекта"""

class Auto():

    color = 'red'
    weight = 1500

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f'Car {self.brand} {self.mark} drives')

    def stop(self):
        print(f'Car {self.brand} {self.mark} stops')

    def use(self):
       print(f'Car age: {self.age + 1}')

auto_info_1 = Auto('Volvo', 2010, 'XC60')
auto_info_2 = Auto('Chrysler', 2006, '300C')
auto_info_1.drive()
auto_info_1.stop()
auto_info_1.use()
auto_info_2.drive()
auto_info_2.stop()
auto_info_2.use()