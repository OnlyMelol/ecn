# coding = utf-8
'''
Created on 2022/07/08

@author: Dustin Lin
'''
import threading, sys
from tools import obj_init_config
from generator import generator
import configparser, os
# from logger import Logger


def pv(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    e0_interval = obj_init_config.get("device_scope_interval", "pv_e0")
    e1_interval = obj_init_config.get("device_scope_interval", "pv_e1")

    list_device_id = device_id
    print(list_device_id)
    for i in range(len(list_device_id)):
        threads.append(
            threading.Thread(target=generator.pv_instance, args=(gene_job, device_id[i], e0_interval,)))
        threads.append(threading.Thread(target=generator.accumulate,
                                        args=(gene_job, device_type, device_id[i], "pv_cumulative", e1_interval,)))
    for i in range(len(threads)):
        threads[i].start()


def battery(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    a4_interval = obj_init_config.get("device_scope_interval", "battery_a4")
    a5_interval = obj_init_config.get("device_scope_interval", "battery_a5")
    a8_interval = obj_init_config.get("device_scope_interval", "battery_a8")
    a9_interval = obj_init_config.get("device_scope_interval", "battery_a9")
    d6_interval = obj_init_config.get("device_scope_interval", "battery_d6")
    d8_interval = obj_init_config.get("device_scope_interval", "battery_d8")
    e2_interval = obj_init_config.get("device_scope_interval", "battery_e2")
    e4_interval = obj_init_config.get("device_scope_interval", "battery_e4")

    threads.append(
        threading.Thread(target=generator.battery_instance, args=(gene_job, device_id, e4_interval)))
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "battery_char_elec_eneg", a4_interval)))
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "battery_dischar_elec_eneg", a5_interval)))
    threads.append(threading.Thread(target=generator.accumulate, args=(
    gene_job, device_type, device_id, "battery_ac_cumu_char_elec_eneg", a8_interval)))
    threads.append(threading.Thread(target=generator.accumulate, args=(
    gene_job, device_type, device_id, "battery_ac_cumu_dischar_elec_eneg", a9_interval)))
    threads.append(threading.Thread(target=generator.accumulate, args=(
    gene_job, device_type, device_id, "battery_cumu_char_elec_eneg", d6_interval)))
    threads.append(threading.Thread(target=generator.accumulate, args=(
    gene_job, device_type, device_id, "battery_cumu_dischar_elec_eneg", d8_interval)))
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "battery_elec_1", e2_interval)))
    for i in range(len(threads)):
        threads[i].start()


def fc(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    c4_interval = obj_init_config("device_scope_interval", "fc_c4")
    c5_interval = obj_init_config("device_scope_interval", "fc_c5")
    threads.append(
        threading.Thread(target=generator.fc_instance, args=(gene_job, device_id, c4_interval,)))
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "fc_cumulative", c5_interval,)))
    for i in range(len(threads)):
        threads[i].start()


def pdb(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    c0_interval = obj_init_config("device_scope_interval", "pdb_c0")
    c1_interval = obj_init_config("device_scope_interval", "pdb_c1")
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "pdb_cumu_normal", c0_interval)))
    threads.append(threading.Thread(target=generator.accumulate,
                                    args=(gene_job, device_type, device_id, "pdb_cumu_reverse", c1_interval)))
    for i in range(len(threads)):
        threads[i].start()


if __name__ == '__main__':
    setup_config = configparser.ConfigParser()
    str_setup_config_path = os.path.join(os.getcwd(), "ini", "device_setting.ini")
    setup_config.read(str_setup_config_path)

    str_battery_instance = setup_config.get("battery", "instance")
    list_battery_instance = str_battery_instance.split(",")
    bool_battery_run = setup_config.getboolean("battery", "run")

    str_pv_instance = setup_config.get("pv", "instance")
    list_pv_instance = str_pv_instance.split(",")
    bool_pv_run = setup_config.getboolean("pv", "run")

    str_pdb_instance = setup_config.get("pdb", "instance")
    list_pdb_instance = str_pdb_instance.split(",")
    bool_pdb_run = setup_config.getboolean("pdb", "run")

    str_fc_instance = setup_config.get("fc", "instance")
    list_fc_instance = str_fc_instance.split(",")
    bool_fc_run = setup_config.getboolean("fc", "run")

    if bool_battery_run:
        battery('battery', list_battery_instance)
    else:
        pass

    if bool_pv_run:
        pv('pv', list_pv_instance)
    else:
        pass

    if bool_pdb_run:
        pdb('pdb', list_pdb_instance)
    else:
        pass

    if bool_fc_run:
        fc('fc', list_fc_instance)
    else:
        pass



