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


class InvalidInt(Exception):
    pass

class InvalidFloat(Exception):
    pass

class InvalidStr(Exception):
    pass


class Queue():
    queue = []

    def add(self, *agrs):
        for i in agrs:
            try:
                if isinstance(i, int):
                    '''проверка условия №1: число делится на 8, состоит из не более 4 символов'''
                    if not i % 8 and len(str(i)) <= 4:
                        self.queue.append(i)
                    else:
                        raise InvalidInt
                elif isinstance(i, float):
                    '''проверка условия №2: у числа с запятой не более 3 символов после запятой'''
                    if round(i, 3) == i:
                        self.queue.append(i)
                    else:
                        raise InvalidFloat
                elif isinstance(i, str):
                    '''проверка условия №3: ксом строка, то длина не более 4 символов без дублирования символов'''
                    a = 0
                    for c in i:
                        if i.count(c) > 1:
                            a = i.count(c) 
                    if len(i) <= 4 and a < 2:
                        self.queue.append(i)
                    else:
                        raise InvalidStr
            except InvalidInt:
                print(f'{i} Число не делиться на 8 или состоит более чем из 4 знаков')
            except InvalidFloat:
                print(f'{i} Число содержит более 2 символов после запятой')
            except InvalidStr:
                print(f'{i} Строка более 4 знаков или содержит 2 повторяющихся знака')
        print(f'{self.queue}')


q = Queue()
q.add(15, 4800, 48000, 'name', 'age', 'id_name', 'agge')