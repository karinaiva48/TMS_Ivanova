"""3. Реализуйте класс DataObject который имеет обязательный атрибут data (произвольного типа данных)
Реализуйте класс очередь (Deque) с атрибутом класса deque в котором будут хранится элементы добавляемые в очередь, 
Класс Deque имеет методы 
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса DataObject (и его дочерних),
а также проверку длины очереди — одновременно там может находится не более 5 элементов — в случае добавления 6 элемента добавление 
не производится и пользователю выдается сообщение о переполнении очереди). 
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod)
"""


from typing import Any
from dataclasses import dataclass

@dataclass
class DataObject:
    data: Any

data_1 = DataObject('first')
data_2 = DataObject('second')
data_3 = DataObject('third')
data_4 = DataObject('fourth')
data_5 = DataObject('fifth')

class Deque:
    deque = []

    @classmethod
    def append_left(cls, obj: DataObject):
        """
        Метод добавляет элемент класса DataObject слева
        """
        if len(cls.deque) < 5:
            if isinstance(obj, DataObject):
                cls.deque.insert(0, obj.data)
                return cls.deque
        else:
            print('No place in line')
            return cls.deque

    @classmethod
    def append_right(cls, obj: DataObject):
        """
        Метод добавляет элемент класса DataObject справа
        """
        if len(cls.deque) < 5:
            if isinstance(obj, DataObject):
                cls.deque.append(obj.data)
                return cls.deque
        else:
            print('No place in line')
            return cls.deque

    @classmethod
    def pop_left(cls):
        """
        Метод удаляет элемент слева и возвращает его
        """
        return cls.deque.pop(0), cls.deque

    @classmethod
    def pop_right(cls):
        """
        Метод удаляет элемент справа и возвращает его
        """
        return cls.deque.pop(-1), cls.deque


print(Deque.append_left(data_1))
print(Deque.append_right(data_2))
print(Deque.append_right(data_3))
print(Deque.append_right(data_4))
print(Deque.append_right(data_5))
print(Deque.append_left(data_1)) 
print(Deque.pop_left())
print(Deque.append_left(data_1))
print(Deque.pop_right())