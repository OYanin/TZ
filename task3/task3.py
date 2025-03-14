from sys import argv
import json

f_tests_name = f_values_name = f_report_name = ''

for a in argv:
    if a.find('tests.json') > -1:
        f_tests_name = a
    elif a.find('values.json') > -1:
        f_values_name = a
    elif a.find('report.json') > -1:
        f_report_name = a

with open(f_tests_name, "r") as f_tests:
    data_tests = json.load(f_tests)

with open(f_values_name, "r") as f_values:
    data_values = json.load(f_values)

tmp_values = {} #упрощенный словарь для обновления значений объектов {id: value}
for i in data_values['values']:
    tmp_values.setdefault(i['id'], i['value'])

def parse_json(data):    
    id = None
    for key, value in data.items():        
        if key == 'id':
            id = value
        if isinstance(value, dict):
            parse_json(value)
        elif isinstance(value, list):
            for val in value:
                parse_json(val)
        else:
            if key == 'value' and id in tmp_values.keys():
                data[key] = tmp_values[id]
            else:
                data[key] = value

for i in data_tests['tests']:
    parse_json(i)

with open(f_report_name, "w") as f_report:
    json.dump(data_tests, f_report)