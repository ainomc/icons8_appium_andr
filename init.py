# -*- coding: utf-8 -*-
"""Initialization module.
    Parsed arguments from command line, like : '-platformName Android'
    Write this data to the param.json
    And run tests
    """


import json
import os
import glob
import argparse
from sys import platform

# python3 init.py --platformName Android --platformVersion 5.1.1 --deviceName Android Emulator --browserName Chrome --homepage https://demo.icons8.com/

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

# Install chrome on device
chrome_apk_path = PATH('chrome_apk/com.android.chrome.apk')
os.system('../../Android/Sdk/platformAndroid-tools/adb install ' + chrome_apk_path)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-platformName', '--platformName', nargs='+', type=str)
parser.add_argument('-platformVersion', '--platformVersion', nargs='+', type=str)
parser.add_argument('-deviceName', '--deviceName', nargs='+', type=str)
parser.add_argument('-browserName', '--browserName', nargs='+', type=str)
parser.add_argument('-homepage', '--homepage', nargs='+', type=str)
args = parser.parse_args()


# Write arguments to the param.json
with open('param.json', 'r+') as outfile:
    json_data = json.load(outfile)
    json_data['platformName'] = args.platformName[0]
    json_data['platformVersion'] = args.platformVersion[0]
    json_data['deviceName'] = args.deviceName[0]
    json_data['browserName'] = args.browserName[0]
    json_data['homepage'] = args.homepage[0]
    outfile.seek(0)
    outfile.write(json.dumps(json_data))
    outfile.truncate()


report_junitxml_path = PATH('report_junit/report')
list_test_fies = glob.glob(os.path.join(os.getcwd(), 'tests', 'tests_*'))

# Convert path to universal path what can be used in linux
for file_num in range(len(list_test_fies)):
    list_test_fies[file_num] = \
        os.path.join(os.getcwd(), 'tests', list_test_fies[file_num])

# Convert list to one string with spaces (' ') between each path
str_list = " ".join(str(x) for x in list_test_fies)

# If you need start only one test file change str_list on like this:
# str_list = os.path.join(os.getcwd(), 'tests', 'tests_x_page.py')

# Run tests with all tests files
if "win" in platform:
    report_junitxml_path = PATH('report_junit/report')
    os.system(r'python3 -m pytest -v %s -s -l --html=%s' % (str_list, report_junitxml_path))

elif "linux" in platform:
    report_junitxml_path = os.path.join(os.getcwd(), 'report_junitxml', ' ')[:-1] + 'report.xml'
    os.system(r'python3 -m pytest -v %s -s -l --junitxml=%s' % (str_list, report_junitxml_path))