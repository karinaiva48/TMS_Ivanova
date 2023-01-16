""" 2. Реализуйте свой пользовательский класс итератора с именем MySquareIterator,
который дает квадраты элементов коллекции, по которой он итерируется.
Пример:
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
	 print(el)
1 4 9 16 25 """

class MySquareIterator:
    def __init__(self, iterable) -> None:
        self.iter = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.iter[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
        return result ** 2

lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
    print(el)