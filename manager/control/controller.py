from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject,Signal,Slot

from view.mainwindow import mainWindow
from business.configManager import configManager
from business.unixClient import unixClient
from business.utils import pathOperationType,envorimentVariables

import time

class Controller(QObject):

    def __init__(self,window:mainWindow):
        self.mainInterface = window
        self.connectSignalsAndSlots()

        self.configManager = configManager()
        self.socket = envorimentVariables.unix_socket_file.value[0]
        self.running = False

    def connectSignalsAndSlots(self):
        self.mainInterface.startWorker.connect(self.sendConfigs_to_Worker)
        self.mainInterface.closeWorker.connect(self.close_Worker)
        self.mainInterface.saveConfig.connect(self.saveConfigs)

        self.mainInterface.pathOperation.connect(self.receive_folder)
        self.mainInterface.filesOperation.connect(self.receive_files)

    @Slot(dict)
    def sendConfigs_to_Worker(self,configs:dict):
        print("sending configurations to worker")
        self.configManager.fillCurrentFile(configs)
        self.running = True
        command = {"running": self.running, "mode": 1,"image_change":False}
        unixClient(self.socket,command)

        # self.__backToNormalMode()

    @Slot()
    def close_Worker(self):
        print("Close worker")

        self.running = False
        command = {"running":self.running,'mode':0}
        unixClient(self.socket,command)

    @Slot()
    def saveConfigs(self):
        print("Save configurations in settings.json")
        self.configManager.saveSettingsFile()

    @Slot(pathOperationType,str)
    def receive_folder(self,operation:pathOperationType, folder: str):
        print(f"{operation.value} : {folder}")
        self.configManager.addfolderInImageList(folder)

        command = {"running": self.running , "mode": 1, "image_change": True}
        unixClient(self.socket,command)

        # self.__backToNormalMode()

    @Slot(pathOperationType,list)
    def receive_files(self,operation:pathOperationType,files: list):
        print(f"{operation.value} : {files}")
        self.configManager.addImagesInImageList(files)

        command = {"running":self.running, "mode": 1, "image_change": True}
        unixClient(self.socket,command)

        # self.__backToNormalMode()


    def __backToNormalMode(self):
        time.sleep(0.2)
        command = {"running": self.running, "mode":0}
        unixClient(self.socket,command)
