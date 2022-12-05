import json
import csv

json_name = input('Введите имя файла JSON или укажите путь к файлу:' )
with open(f'{json_name}.json', 'r') as file:
    json_string = json.load(file)

def transform_to_csv(json_string: str):
    user_id = []
    names = []
    ages = [] 
    for key, value in json_string.items():
        user_id.append(key)
        for keys, values in value.items():
            if keys == 'name':
                names.append(values)
            else:
                ages.append(values)

    obj_list = list(zip(names, ages, user_id))
    csv_name = input('Введите название CSV файла в который желаете сохранить данные:')
    with open(f'{csv_name}.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(['name', 'age', 'id'])
        for i in obj_list:
            csv_writer.writerow(list(i)) 

transform_to_csv(json_string)