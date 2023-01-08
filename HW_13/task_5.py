""" Реализуйте генератор, который будет бесконечно генерировать числа Фибоначчи (https://en.wikipedia.org/wiki/Fibonacci_number).
Пример:
>>> gen = endless_fib_generator()
>>> while True:
	print(next(gen))
>>> 1 1 2 3 5 8 13 ...
"""


def endless_fib_gen():
    x, y = 3, 6
    while True:
        yield y
        x, y = y, x + y

        
gen = endless_fib_gen()
for i in range(5):
    print(next(gen))

