from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject,Signal,Slot
from view.mainwindow import mainWindow

class Controller(QObject):

    def __init__(self,window:mainWindow):
        self.mainInterface = window
        self.connectSignalsAndSlots()

    def connectSignalsAndSlots(self):
        self.mainInterface.startWorker.connect(self.sendConfigs_to_Worker)
        self.mainInterface.closeWorker.connect(self.close_Worker)
        self.mainInterface.saveConfig.connect(self.saveConfigs)

    @Slot()
    def sendConfigs_to_Worker(self):
        print("sending configurations to worker")
    
    @Slot()
    def close_Worker(self):
        print("Close worker")

    @Slot()
    def saveConfigs(self):
        print("Save configurations in settings.json")