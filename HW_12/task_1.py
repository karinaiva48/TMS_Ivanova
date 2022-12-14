"""1) Создайте интерактивный калькулятор.
Пользовательский ввод представляет собой формулу, состоящую из числа, оператора (+,-,*,/,**) и другого 
числа, разделенных пробелом (например, 1 + 1). Проверьте input по следующим правилам:
1. Если входные данные не состоят из 3 действительных элементов, вызовите InputFormulaError, которая является пользовательским исключением.
2. Если первый и третий элемент не являются действительными числами — выводится ошибка InputNumberError.
3. Если второй элемент не соответствует поддерживаемым операторам — выводится ошибка InputOperatorError.
Если ввод верен, выполните вычисление и выведите результат (в случае возникновения ошибки при вычислении — 
также выводим ее). Затем пользователю предлагается ввести новый ввод и так далее, пока пользователь не введет quit.
Взаимодействие может выглядеть так:
>>> 1 + 1
2.0
>>> 3,2 - 1,5
1.70
>>> quit
"""

class InputFormulaError(Exception):
    pass
class InputNumberError(Exception):
    pass
class InputOperatorError(Exception):
    pass


while True:
    expression = input ('Введите формулу, состоящую из числа, оператора (+,-,*,/,**) и другого числа, разделенных пробелом, например, (1 + 1): ')
    if expression == 'quite':
        break
    new_expression = expression.split(' ')
    num_1, num_2 = new_expression[0], new_expression[2]
    operator = new_expression[1]
    if len(new_expression) > 3:
        raise InputFormulaError('Превышено количество символов!')
    try:
        num_1, num_2 = float(num_1), float(num_2)
    except ValueError:
        raise InputNumberError('Введеные символов не являются числами!')
    if operator not in ('+', '-', '*', '/', '**'):
        raise InputOperatorError ('Вы ввели неверный оператор!')
    if new_expression[1] == '+':
        print (num_1 + num_2)
    elif new_expression[1] == '-':
        print (num_1 - num_2)
    elif new_expression[1] == '/':
        print (round(num_1 / num_2), 2)
    elif new_expression[1] == '*':
        print (num_1 * num_2)
    elif new_expression[1] == '**':
        print (num_1 ** num_2)
    else:
        raise InputOperatorError('Не известный оператор!')
    
