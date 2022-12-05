""" 2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto. Класс Truck имеет дополнительный обязательный атрибут max_load. 
Переопределить метод drive, который перед появление сообщения «Car <brand> <mark> drives» выводит сообщение «Attention!». 
Реализовать дополнительный метод load. При его вызове происходит пауза в 1 секунду (используя модуль time), затем выводится сообщение «load», 
а затем снова происходит пауза в 1 секунду.
Класс Sedan имеет дополнительный метод обязательный атрибут max_speed и при вызове метода drive, после появления сообщения «Car <brand> <mark> drives»,
выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>». Инициализировать по 2 отдельных объекта этих классов,
проверить работы их методов и атрибутов (вызвать методы, атрибуты вывести в печать)"""

import time

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

class Truck(Auto):

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def drive(self):
        print('Attention!')
        print(f'Car: {self.brand} {self.mark} drives')
    
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Sedan(Auto):

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def drive(self):
        print(f'Car: {self.brand} {self.mark} drives')
        print(f'max speed of {self.brand} {self.mark} is {self.max_speed}')

truck_info = Truck('Some Big Truck', 5, '***', 100500)
sedan_info = Sedan('Volvo', 12, 'XC60', 280)
truck_info.drive()
truck_info.load()
sedan_info.drive()

print(truck_info.max_load)
print(sedan_info.max_speed)