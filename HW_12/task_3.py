"""
3*) Создайте класс, который имеет атрибут queue (допускается использование списка) который имеет метод add позволяющий добавлять в queue следующие объекты — целые числа, числа с плавающей запятой, строки.
При этом в момент добавления происходит валидация элементов по следующим правилам:
1. Целые числа — должны делится на 8, состоять из не более чем 4 символов
2. Числа с запятой — не более 3 символов после запятой
3. Строки — длина не более 4 символов без дублирования символов
В результате работы метода add элементы прошедшие валидацию добавляются в queuе, элементы не прошедшие валидацию  выводятся пользователю с сообщением о причине недобавления, например
q=Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, text, data, world)
InvalidIntDivision → 1 # не делится на 8
InvalidIntNumberCount → 80000 # больше 4 символов
"""


class InvalidIntDivision(Exception):
    pass


class InvalidIntNumberCount(Exception):
    pass


class InvalidFloatNumber(Exception):
    pass


class InvalidStr(Exception):
    pass


class Queue:
    """
    Класс позволяет добавлять в метод add элементы и делать проверку валидации входных данных
    """

    def __init__(self):
        self.queue = []

    def add(self, *args):
        for i in args:
            try:
                if isinstance(i, int):  # проверка на целое число
                    if i % 8 == 0:  # проверка делится ли число на 8
                        if len(str(i)) <= 4:  # длина числа должна быть 4 или меньше
                            self.queue.append(i)
                        else:
                            raise InvalidIntNumberCount  # если длина больше выводится ошибка
                    else:
                        raise InvalidIntDivision  # если не делится выводится ошибка
                elif isinstance(i, float):  # проверка на вещественное ли это число
                    s = str(i)  # переводим float в строку для нахождения точки в нем
                    index = s.find(".")  # находим точку в числе
                    s = s[index + 1:]  # от индекса + 1 заносим в переменную s определенное количество символов
                    if len(s) <= 3:  # если элементов 3 и меньше после точки добавляем в список
                        self.queue.append(i)
                    else:  # иначе вызываем ошибку если элементов больше 3 после точки
                        raise InvalidFloatNumber
                elif isinstance(i, str):  # проверка на строку
                    if len(i) == len(set(i)):
                        self.queue.append(i)  # добавляем в список
                    else:
                        raise InvalidStr  # иначе если не подходит условию делаем ошибку
            except InvalidIntDivision:
                print(i, "-> не делится на 8")
            except InvalidIntNumberCount:
                print(i, "-> больше 4 символов")
            except InvalidFloatNumber:
                print(i, "-> больше 3 символов после запятой")
            except InvalidStr:
                print(i, "-> больше 4 символов или есть дублирование символа")


q = Queue()
q.add(1, 16, 280, 1.82, "wordd", 1.8345, "text", 80000)