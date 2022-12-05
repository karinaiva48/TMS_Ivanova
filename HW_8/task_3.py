#! bin/bash

file = open('/home/karinaiva48/TMS/HW_8/unsorted_names.txt', 'r')
sorted_file = sorted(file.readlines())
file.close()

new_file = open('/home/karinaiva48/TMS/HW_8/sorted_names.txt', 'w')
new_file.write(''.join(sorted_file))
new_file.close()



