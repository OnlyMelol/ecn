#coding=utf-8
"""
Created on: 2022/07/12

@author: Dustin Lin
"""
import os
import datetime
import logging.handlers

obj_now = datetime.datetime.now()

def Logger(type, level, msg):
    obj_root_logger = logging.getLogger(type)

    bool_debug = True
    bool_console_msg = True
    bool_file_msg = True

    # Log level: DEBUG < INFO < WARNING < ERROR < CRITICAL
    debug_level = 'DEBUG'
    str_log_format = "%(asctime)s - %(process)d:%(thread)d - [%(levelname)s][%(name)s] %(message)s"

    if not bool_debug:
        obj_root_logger.disabled = True
    else:
        if debug_level == 'DEBUG':
            obj_root_logger.setLevel(logging.DEBUG)
        elif debug_level == 'INFO':
            obj_root_logger.setLevel(logging.INFO)
        elif debug_level == 'WARNING':
            obj_root_logger.setLevel(logging.WARNING)
        elif debug_level == 'ERROR':
            obj_root_logger.setLevel(logging.ERROR)
        elif debug_level == 'CRITICAL':
            obj_root_logger.setLevel(logging.CRITICAL)

    if bool_console_msg:
        formatter = logging.Formatter(str_log_format)
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        obj_root_logger.addHandler(console)

    if bool_file_msg:
        formatter = logging.Formatter(str_log_format)
        file_title = obj_now.strftime("%Y_%m_%d___%H_%M_%S_%f")
        log_file = os.path.join(os.getcwd(), 'history', f'{file_title}.log')
        obj_log_file = logging.handlers.RotatingFileHandler(log_file, mode = 'a', maxBytes = 10485760, backupCount = 20, encoding = 'utf8')
        obj_log_file.setFormatter(formatter)
        obj_root_logger.addHandler(obj_log_file)

    if level == 'DEBUG':
        return obj_root_logger.debug(msg)
    elif level == 'INFO':
        return obj_root_logger.info(msg)
    elif level == 'WARNING':
        return obj_root_logger.warning(msg)
    elif level == 'ERROR':
        return obj_root_logger.error(msg)
    elif level == 'CRITICAL':
        return obj_root_logger.critical(msg)

if __name__ == '__main__':
    pass