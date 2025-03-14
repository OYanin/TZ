import os.path
import os
from sys import argv
import json

#f_tests_name = argv[argv.index('tests.json')]
#f_values_name = argv[argv.index('values.json')]
#f_report_name = argv[argv.index('report.json')]

f_tests_name = os.path.abspath('tests.json')

print(os.path.dirname(os.path.abspath('tests.json')))

print(f_tests_name)
print(os.getcwd())

#with open(f_tests_name, "r") as f_tests:
#    json.load(f_tests)

