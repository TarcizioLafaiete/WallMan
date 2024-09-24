from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal,Slot

from .forms.ui_mainwindow import Ui_MainWindow
from business.utils import pathOperationType,envorimentVariables

import json


class mainWindow(QMainWindow):

    startWorker = Signal(dict)
    closeWorker = Signal()
    saveConfig = Signal(dict)
    pathOperation = Signal(pathOperationType,str)
    filesOperation = Signal(pathOperationType,list)
    

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resouces = envorimentVariables.resourses_dir.value
        self.currentSettingsFile = envorimentVariables.current_settings_json.value[0]
        self.settingsFile = envorimentVariables.settings_json.value[0]


        self.__readCurrentSettings()
        self.connectSignalsAndSlots()
        self.ui.start_button.setStyleSheet("background-color: #00AA00")
        self.ui.close_button.setStyleSheet("background-color: #AA0000")

        self.__setIcons(self.ui.add_folder,self.resouces + '/adicionar-pasta.png')
        self.__setIcons(self.ui.ignore_folder,self.resouces + '/adicionar-pasta.png')
        self.__setIcons(self.ui.remove_folder,self.resouces + '/remover-pasta.png')

        self.__setIcons(self.ui.add_file, self.resouces + '/adicionar-imagem.png')
        self.__setIcons(self.ui.ignore_file,self.resouces + '/adicionar-imagem.png')
        self.__setIcons(self.ui.remove_file,self.resouces + '/remover-imagem.png')


    def connectSignalsAndSlots(self):
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.close_button.clicked.connect(self.close_button_clicked)
        self.ui.save_button.clicked.connect(self.saveConfig_button_clicked)

        self.ui.add_folder.clicked.connect(self.get_add_folder)
        self.ui.ignore_folder.clicked.connect(self.get_ignore_folder)
        self.ui.remove_folder.clicked.connect(self.get_remove_folder)

        self.ui.add_file.clicked.connect(self.get_add_files)
        self.ui.ignore_file.clicked.connect(self.get_ignore_files)
        self.ui.remove_file.clicked.connect(self.get_remove_files)

    @Slot()
    def start_button_clicked(self):
        self.startWorker.emit(self.__getConfigs())

    @Slot(str)
    def close_button_clicked(self):
        self.closeWorker.emit()

    @Slot()
    def saveConfig_button_clicked(self):
        self.saveConfig.emit(self.__getConfigs())

    @Slot()
    def get_add_folder(self):
        self.pathOperation.emit(pathOperationType.ADD,self.__get_folder())

    @Slot()
    def get_ignore_folder(self):
        self.pathOperation.emit(pathOperationType.IGNORE,self.__get_folder())

    @Slot()
    def get_remove_folder(self):
        self.pathOperation.emit(pathOperationType.REMOVE,self.__get_folder())

    @Slot()
    def get_add_files(self):
        self.filesOperation.emit(pathOperationType.ADD,self.__get_files())

    @Slot()
    def get_ignore_files(self):
        self.filesOperation.emit(pathOperationType.IGNORE,self.__get_files())

    @Slot()
    def get_remove_files(self):
        self.filesOperation.emit(pathOperationType.REMOVE,self.__get_files())

    def __get_folder(self):
        folder_name = QFileDialog.getExistingDirectory()
        return folder_name
    
    def __get_files(self):
        files_names, _ = QFileDialog.getOpenFileNames()
        return files_names
        

    def __readCurrentSettings(self):
        with open(self.settingsFile,'r') as file:
            settings = json.load(file)

        self.ui.time_edit.setText(str(settings['time']))
        self.ui.time_unit_box.setCurrentText(settings['time_unit'])
        self.ui.ui_system_box.setCurrentText(settings['ui_system'])

        self.ui.ignore_checkBox.setChecked(settings['ignore_images'])
        self.ui.random_checkBox.setChecked(settings['random_display'])

        with open(self.currentSettingsFile,'w') as file:
            json.dump(settings,file,indent=4)

    def __setIcons(self,object,resource):
        icon = QIcon(resource)
        object.setIcon(icon)
        object.setText('')

    def __getConfigs(self):
        configDict = {
            'time': int(self.ui.time_edit.toPlainText()),
            'time_unit': self.ui.time_unit_box.currentText(),
            'ui_system': self.ui.ui_system_box.currentText(),
            'ignore_images': self.ui.ignore_checkBox.isChecked(),
            'random_display': self.ui.random_checkBox.isChecked()
        }
        return configDict