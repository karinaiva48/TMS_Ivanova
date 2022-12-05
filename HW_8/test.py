import csv, json

with open('/home/karinaiva48/TMS/HW_8/file_json.json', 'r') as file_json:
    file_json_on_form = json.load(file_json)

def transform_to_csv(file_json_on_format):
    keys_id = file_json_on_format.keys()
    file_json_to_format_list = list(file_json_on_format)
  
    data_to_csv = []
    i = 0
    for x in keys_id:
        data_to_csv[i].append()
    with open('/home/karinaiva48/TMS/HW_8/file48.csv', 'wt') as file_csv:
        csv_out = csv.writer(file_csv)
        csv_out.writerows(list(file_json_on_format))

transform_to_csv(file_json_on_form)