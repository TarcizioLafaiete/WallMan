#!/bin/python3

import time
import os
import threading
import json
import random
import signal
import numpy as np

from utils.unixServer import unixServer


unixFile = os.getenv("UNIX_SOCKET_FILE")
currentSettingsFile = os.getenv("CURRENT_SETTINGS_JSON")
settingsFile = os.getenv("SETTINGS_JSON")
wallman_root = os.getenv("WALLMAN_ROOT")

commandDict = {'running':0,'mode':0}

new_request = False
reset_socket = False

mutex = threading.Lock()

def handle_sigterm(signum):
    global reset_socket
    reset_socket = True    

signal.signal(signal.SIGTERM,handle_sigterm)

def socket_routine():
    server = unixServer(unixFile)

    while True:
        global reset_socket
        if reset_socket:
            server.close()
            server = unixServer(unixFile)
            reset_socket = False

        server.accept()
        mutex.acquire()
        global commandDict
        commandDict = server.recvMessage()
        global new_request
        new_request =  True
        mutex.release()

def custom_sleep(seconds):
    global new_request
    start_time = time.time()
    passed_time = time.time() - start_time

    while passed_time < seconds:
        time.sleep(0.033)
        passed_time = time.time() - start_time

        if new_request:
            mutex.acquire()
            new_request = False
            mutex.release()
            return seconds - passed_time
    return 0

def generate_imagesList(settings:dict) -> list[str]:
    current_carousel = settings['current_carousel']
    imagesList = settings[str(current_carousel)]
    return imagesList

def getOtherConfigs(settings:dict) -> dict:
    return {'time':settings['time'],
            'time_unit': settings['time_unit'],
            'ui': settings['ui_system'],
            'random': settings['random_display']
            }

def convertTimeUnit(unit:str):
    if unit == 'sec':
        return 1
    elif unit == 'min':
        return 60
    elif unit == 'hour':
        return 60*60
    elif unit == 'day':
        return 60*60*24
    else:
        return 0

def plotWallpaper(image:str,configs:dict):
    command = ''
    if configs['ui'] == "Gnome":
        command = f"gsettings set org.gnome.desktop.background picture-uri file://{image}"
    elif configs['ui'] == "Kde":
        command = f"bash {wallman_root}/worker/utils/kde_change_wallpaper_command.sh {image}"
    os.system(command)
    return custom_sleep(configs['time'] * convertTimeUnit(configs['time_unit']))

def wallpaper_routine():
    settings = {}

    with open(settingsFile,'r') as file:
        settings = json.load(file)

    configs = getOtherConfigs(settings)
    images = generate_imagesList(settings)
    indexList = 0
    listSize = len(images)
    remaining_time = 0

    running = 0

    while True:
        mutex.acquire()
        global commandDict
        commandFlags = commandDict
        mutex.release()

        if commandFlags['running'] != 2:
            running = commandFlags['running']

        if running:
            if commandFlags['mode'] == 0:
                if listSize > 0:
                    if remaining_time == 0:
                        indexList = ((indexList + 1) + (random.randint(0,listSize) * configs['random'])) % listSize
                        remaining_time = plotWallpaper(images[indexList],configs) 
                    else:
                        remaining_time = custom_sleep(remaining_time)
        
        if commandFlags['mode'] == 1:

            with open(currentSettingsFile,'r') as file:
                settings = json.load(file)

            if commandFlags['image_change'] == False:
                configs = getOtherConfigs(settings)
                remaining_time = 0
            images = generate_imagesList(settings)
            listSize = len(images)

            commandFlags['mode'] = 0

        elif commandFlags['mode'] == 2:
            if listSize > 0:
                plot_configs = {'time':1, 'time_unit':'sec','ui':configs['ui']}
                remaining_time = 0
                plotWallpaper(commandFlags['image'],plot_configs)

def main():
    socketTherad = threading.Thread(target=socket_routine)
    wallpaperTherad = threading.Thread(target=wallpaper_routine)
    
    socketTherad.start()
    wallpaperTherad.start()
    
if __name__ == "__main__":
    main()
