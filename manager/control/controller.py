from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject,Signal,Slot
from view.mainwindow import mainWindow
from business.configManager import configManager
from business.unixClient import unixClient

class Controller(QObject):

    def __init__(self,window:mainWindow):
        self.mainInterface = window
        self.connectSignalsAndSlots()

        self.configManager = configManager()
        self.initial = True

    def connectSignalsAndSlots(self):
        self.mainInterface.startWorker.connect(self.sendConfigs_to_Worker)
        self.mainInterface.closeWorker.connect(self.close_Worker)
        self.mainInterface.saveConfig.connect(self.saveConfigs)

    @Slot(dict)
    def sendConfigs_to_Worker(self,configs:dict):
        print("sending configurations to worker")
        self.configManager.fillCurrentFile(configs)
        command = {"flag": 1,"initial": self.initial,"image_change":False}
        unixClient('/tmp/socket_file',command)
        
        self.initial = False
    
    @Slot()
    def close_Worker(self):
        print("Close worker")
        command = {"flag": 0}
        unixClient('/tmp/socket_file',command)

    @Slot()
    def saveConfigs(self):
        print("Save configurations in settings.json")
        self.configManager.saveSettingsFile()