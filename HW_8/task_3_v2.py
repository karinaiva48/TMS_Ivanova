#! bin/bash
with open('unsorted_names.txt', 'r') as first_file, open('sorted_names2.txt', 'w') as file:
    file.write(first_file.read())
file_unsort = open('/home/karinaiva48/TMS/HW_8/sorted_names2.txt', 'r')
sorted_file = sorted(file_unsort.readlines())
file.close()