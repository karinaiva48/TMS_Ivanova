#! bin/bash
import random

name = 'Tim,John,Sally,Trevor,Harry'
age = (12,34,24,57,18)
my_dict = dict(zip(name.split(','), age))
#print(my_dict)

new_dict = {}
for key, value in my_dict.items():
    id = random.randint(100000, 999999)
    new_dict[id] = {'name': key, 'age': value}
#print(new_dict)

import json
with open('file_json.json', 'w') as file:
    json_file = json.dump(new_dict, file)