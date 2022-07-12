#coding=utf-8
"""
Created on: 2022/07/08

@author: Dustin Lin
"""
import os
import datetime
import configparser
import requests
from logger import Logger

# For log recording...
now = datetime.datetime.now()
# Import initial data value & API config, etc...
obj_init_config = configparser.ConfigParser()
str_config_path = os.path.join(os.getcwd(), "conf", "device_data.conf")
obj_init_config.read(str_config_path)

# For API post request
def send_request(str_url, str_data):
    dict_headers = eval(obj_init_config.get('api_info', 'request_header'))
    obj_response = requests.put(str_url, json = {'edt': str_data}, headers = dict_headers)
    dict_response = obj_response.json()
    Logger('Request', 'INFO', str(dict_response))

def verify_init_value_isexist(task, scope):
    if obj_init_config.has_section(task) is True:
        pass
    else:
        init_config_set_section(task)
    if obj_init_config.has_option(task , scope) is True:
        Logger('InitData', 'INFO', 'Already has init value')
    else:
        Logger('InitData', 'INFO', f"""Config add -> section: {task}; key: {scope}""")
        init_config_set(task, scope, "400")

def init_config_set_section(section):
    obj_init_config.add_section(section)

def init_config_set(section, scope, value):
    obj_init_config.set(section, scope, value)
    obj_init_config.write(open(str_config_path, 'w'))

def init_config_get(section, scope):
    return obj_init_config.get(section, scope)

if __name__ == '__main__':
    test = obj_init_config.get("test", "pv")
    print(test)

