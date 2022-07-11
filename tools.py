#coding=utf-8
"""
Created on: 2022/07/08

@author: Dustin Lin
"""
import os
import datetime
import configparser
import requests

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
    print(dict_response)
    write_history(dict_response)

def write_history(data):
    now = (datetime.datetime.now()).strftime("%Y%m%d-%H-%M-%S")
    str_log_path = os.path.join(os.getcwd(), 'history', f'{now}_log.log')
    obj_file = open(str_log_path, 'a')
    obj_file.writelines([str(data) + "\n"])
    obj_file.close()


def verify_init_value_isexist(task, scope):
    if obj_init_config.has_section(task) is True:
        pass
    else:
        init_config_set_section(task)
    if obj_init_config.has_option(task , scope) is True:
        print("Already has init value")
    else:
        print(f"""Config add -> section: {task}; key: {scope}""")
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

# from logger import Logger
# def log_title():
#     date_time = now.strftime("%Y/%m/%d %H:%M:%S.%f")
#     title = "Start from " + date_time
#     print(title)
#
#
# def result(int_data, int_start_data):
#     today_total = str(int_data - int_start_data)
#     today_final = str(int(today_total, 16))
#     msg = str(datetime.datetime.now()) + " today from :{} today total: {} to int: {}".format(int_start_data, (
#                 int_data - int_start_data), today_final) + "\n"
#     # Logger('Result', 'INFO', msg)
#     return msg
#
#
# def write_log_file(insert_data):
#     file_title = now.strftime("%Y_%m_%d__%H_%M_%S_%f") + ".txt"
#     path = os.path.join(os.getcwd(), "log", file_title)
#     f = open(path, 'a')
#     lines = insert_data
#     f.writelines(lines)
#     f.close()
#
#
# def verify_init_value_isexist(task, scope):
#     if config.has_section(task) is True:
#         pass
#     else:
#         config_set_section(task)
#     if config.has_option(task, scope) is True:
#         print("#Already has init value")
#     else:
#         print("#Config add ->session: {} key: {}".format(task, scope))
#         config_set(task, scope, "400")
#
#
# def config_set_section(section):
#     config.add_section(section)
#
#
# def config_set(session, scope, value):
#     config.set(session, scope, value)
#     config.write(open(str_config_path, 'w'))
#
#
# def config_get(session, scope):
#     return config.get(session, scope)
