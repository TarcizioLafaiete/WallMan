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
        command = {"running": 1, "mode": 1,"image_change":False}
        unixClient(self.socket,command)


    @Slot()
    def close_Worker(self):
        print("Close worker")

        command = {"running":0,'mode':0}
        unixClient(self.socket,command)

    @Slot(dict)
    def saveConfigs(self,configs:dict):
        print("Save configurations in settings.json")
        self.configManager.fillCurrentFile(configs)
        self.configManager.saveSettingsFile()

    @Slot(pathOperationType,str)
    def receive_folder(self,operation:pathOperationType, folder: str):
        print(f"{operation.value} : {folder}")
        if not folder:
            return

        self.configManager.addfolderInImageList(folder)

        command = {"running": 2 , "mode": 1, "image_change": True}
        unixClient(self.socket,command)


    @Slot(pathOperationType,list)
    def receive_files(self,operation:pathOperationType,files: list):
        print(f"{operation.value} : {files}")
        if not files:
            return
        
        if operation == pathOperationType.ADD:
            self.configManager.addImagesInImageList(files)
        
        elif operation == pathOperationType.REMOVE:
            self.configManager.removeImageInImageList(files[0])

        command = {"running":2, "mode": 1, "image_change": True}
        unixClient(self.socket,command)
