"""Реализуйте класс итератора EvenRange, который принимает начало и конец интервала в качестве аргументов инициализации и выдает только четные числа во время итерации.
Если пользователь попытается выполнить итерацию после того, как он выдал все возможные числа следует вывести «Out of number!».
_Примечание: вообще не используйте функцию range()_
Пример:
>>> er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
>>> er2 = EvenRange(3, 14)
>>> for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
"""

class EvenRange:
    def __init__(self, start, stop) -> None:
        self.stop = stop
        self.start = start if not start % 2 else start + 1


    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        if result >= self.stop:
            print("Out of numbers!")
            raise StopIteration
        else:
            self.start += 2
            return result

erl = EvenRange(3,13)
for i in erl:
    print(i)
