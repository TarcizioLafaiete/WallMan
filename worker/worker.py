import time
import os
import threading
import json
import random
import numpy as np

from utils.unixServer import unixServer

unixFile = '/tmp/socket_file'
commandDict = {'flag':0}

mutex = threading.Lock()


def socket_routine():
    server = unixServer(unixFile)
    
    while True:
        server.accept()
        mutex.acquire()
        global commandDict
        commandDict = server.recvMessage()
        mutex.release()

def generate_imagesList(settings:dict) -> list[str]:
    imagesList = settings['images_list']
    ignoreList = []
    
    if(settings['ignore_images']):
        ignoreList = settings['ignore_list']

    imagesList = list(set(imagesList) - set(ignoreList))
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
        command = f"utils/kde_change_wallpaper_command.sh {image}"
    os.system(command)
    time.sleep(configs['time'] * convertTimeUnit(configs['time_unit']))


def wallpaper_routine():
    settings = {}

    with open('../settings.json','r') as file:
        settings = json.load(file)

    configs = getOtherConfigs(settings)
    images = generate_imagesList(settings)
    indexList = 0
    listSize = len(images)

    while True:
        mutex.acquire()
        global commandDict
        commandFlags = commandDict
        mutex.release()

        flag = commandFlags['flag']
        if flag == 1:
            if not commandFlags['initial']:

                with open('../currentSettings.json','r') as file:
                    settings = json.load(file)

                if commandFlags['image_change']:
                    images = generate_imagesList(settings)
                    listSize = len(images)
                else:
                    configs = getOtherConfigs(settings)

            plotWallpaper(images[indexList],configs)
            indexList = ((indexList + 1) + (random.randint(0,listSize) * configs['random'])) % listSize
        elif flag == 2:
            plotWallpaper(commandFlags['image'],configs)
            

def main():
    socketTherad = threading.Thread(target=socket_routine)
    wallpaperTherad = threading.Thread(target=wallpaper_routine)

    socketTherad.start()
    wallpaperTherad.start()
    
if __name__ == "__main__":
    main()