from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal,Slot

from .forms.ui_mainwindow import Ui_MainWindow
from .imageList_widget import imageList_Widget
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

        self.imageList_widget = None

        self.resouces = envorimentVariables.resourses_dir.value
        self.currentSettingsFile = envorimentVariables.current_settings_json.value[0]
        self.settingsFile = envorimentVariables.settings_json.value[0]

        self.setWindowIcon(QIcon(self.resouces + '/wallman_icon.jpeg'))

        self.plotedImage = ""

        self.__readCurrentSettings()
        self.connectSignalsAndSlots()
        self.ui.start_button.setStyleSheet("background-color: #00AA00")
        self.ui.close_button.setStyleSheet("background-color: #AA0000")
        self.ui.save_plot_Image.setStyleSheet("background-color:#0000AA")
        self.ui.save_plot_Image.setText("Add Image")
        self.ui.save_plot_Image.setVisible(False)

        self.__setIcons(self.ui.add_folder,self.resouces + '/adicionar-pasta.png')

        self.__setIcons(self.ui.add_file, self.resouces + '/adicionar-imagem.png')
        self.__setIcons(self.ui.remove_file,self.resouces + '/remover-imagem.png')
        self.__setIcons(self.ui.show_image,self.resouces + '/adicionar-imagem.png')


    def connectSignalsAndSlots(self):
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.close_button.clicked.connect(self.close_button_clicked)
        self.ui.save_button.clicked.connect(self.saveConfig_button_clicked)
        self.ui.save_plot_Image.clicked.connect(self.save_image_ploted)

        self.ui.add_folder.clicked.connect(self.get_add_folder)

        self.ui.remove_file.clicked.connect(self.open_imageList_widget)

        self.ui.add_file.clicked.connect(self.get_add_files)
        self.ui.show_image.clicked.connect(self.get_show_image)

    @Slot()
    def start_button_clicked(self):
        if self.ui.save_plot_Image.isVisible():
            self.ui.save_plot_Image.setVisible(False)
        self.ui.start_button.setText("Apply")
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
    def get_add_files(self):
        self.filesOperation.emit(pathOperationType.ADD,self.__get_files())

    @Slot()
    def get_show_image(self):
        self.plotedImage = self.__get_unique_file()
        if len(self.plotedImage) > 0:
            self.ui.save_plot_Image.setVisible(True)
            self.ui.start_button.setText("Restart")
            self.filesOperation.emit(pathOperationType.SHOW,[self.plotedImage])

    @Slot(str)
    def get_remove_image(self,path):
        self.filesOperation.emit(pathOperationType.REMOVE,[path])

    @Slot()
    def get_remove_all_images(self):
        settings = {}
        with open(self.currentSettingsFile, 'r') as file:
            settings = json.load(file)

        self.closeWorker.emit()

        self.filesOperation.emit(pathOperationType.REMOVE,settings['images_list']) 

    @Slot()
    def open_imageList_widget(self):
        if self.imageList_widget is None or not self.imageList_widget.isVisible():
            self.imageList_widget = imageList_Widget()
            self.imageList_widget.remove_image_request.connect(self.get_remove_image)
            self.imageList_widget.remove_all_images_request.connect(self.get_remove_all_images)
            self.imageList_widget.show()

    @Slot()
    def save_image_ploted(self):
        self.ui.save_plot_Image.setVisible(False)
        self.filesOperation.emit(pathOperationType.ADD,[self.plotedImage])

    def __get_folder(self):
        folder_name = QFileDialog.getExistingDirectory()
        return folder_name
    
    def __get_files(self):
        files_names, _ = QFileDialog.getOpenFileNames()
        return files_names
    
    def __get_unique_file(self):
        file,_ = QFileDialog.getOpenFileName()
        return file
         

    def __readCurrentSettings(self):
        with open(self.settingsFile,'r') as file:
            settings = json.load(file)

        self.ui.time_edit.setText(str(settings['time']))
        self.ui.time_unit_box.setCurrentText(settings['time_unit'])
        self.ui.ui_system_box.setCurrentText(settings['ui_system'])
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
            'random_display': self.ui.random_checkBox.isChecked()
        }
        return configDict
