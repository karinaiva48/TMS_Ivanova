""" 3. Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика. 
Если начальное значение не указано, счетчик должен начинаться с 0. Если стоп-значение не указано, оно должно 
считаться вверх бесконечно. Если счетчик достигает стоп-значения, выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)"""

class Counter:
    def __init__(self, start = 0, stop = None) -> None:
        self.start = start
        self.stop = stop

    def increment(self):
        while True:
            self.start += 1
            if self.start == self.stop:
                return print("Maximal value is reached")
          
    def get(self):
        print(self.start)

count = Counter(8,48)
count.increment()
count.get()