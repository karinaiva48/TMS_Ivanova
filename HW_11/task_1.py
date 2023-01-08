"""
1. Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда. 
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа) и дополнительное свойство, 
обозначающее сумму, которую осталось оплатить (с учетом стоимости заказа и внесенных с помощью метода «оплатить» денег)
"""

from dataclasses import dataclass

@dataclass
class Dish():
    """класс содержит характеристику блюд
    """
    amount: int
    name: str
    value: float
    weight: float

dish_1 = Dish(1, 'Fish and chips', 15, 450)
dish_2 = Dish(2,'Crab Cake', 35, 250)

class Order:
    """класс определяет количество, сумму и вес всего заказа
    """
    def __init__(self):
        self.dish = []

    def add_dish(self, dish: Dish):
        self.dish.append(dish)

    @property
    def total_weight(self):
        return sum([dish.weight for dish in self.dish])
    
    @property
    def total_amount(self):
        return len(self.dish)

    @property
    def total_value(self):
        return sum([dish.value for dish in self.dish])

    def pay_money(self, money: float):
        self.payout = self.total_value - money
        if  self.payout > 0:
            print(f'You have to pay {self.payout}$')
        elif self.payout < 0:
            print(f'Your moneyback is {abs(self.payout)}$')
        else:
            print('You owe nothing!')


order = Order()
order.add_dish(dish_1)
order.add_dish(dish_2)
print(order.total_amount)
print(order.total_value)
print(order.total_weight)
order.pay_money(25)