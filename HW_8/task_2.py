#! bin/bash
name = input('Введите Ваше имя:')
family_name = input('Введите Вашу фамилию:')
birth = input('Введите дату Вашего рождения:')
city = input('Введите город проживания:')

with open('task_8_2.txt', 'w') as file:
    data = [name, family_name]
    for line in data:
        file.write(line + '|\n')
with open('task_8_2.txt', 'a') as file:
    data = [birth, city]
    for line in data:
        file.write(line.upper() + '|\n')
