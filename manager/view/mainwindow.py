from PySide6.QtWidgets import QMainWindow, QFileDialog, QInputDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal,Slot

from .forms.ui_mainwindow import Ui_MainWindow
from .imageList_widget import imageList_Widget
from .carouselList_widget import carouselList_Widget
from business.utils import pathOperationType,envorimentVariables

import json


class mainWindow(QMainWindow):

    startWorker = Signal(dict)
    closeWorker = Signal()
    saveConfig = Signal(dict)
    editCarouselName = Signal(str)
    pathOperation = Signal(pathOperationType,str)
    filesOperation = Signal(pathOperationType,list)


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.imageList_widget = None
        self.carouselList_widget = None

        self.resouces = envorimentVariables.resourses_dir.value
        self.currentSettingsFile = envorimentVariables.current_settings_json.value[0]
        self.settingsFile = envorimentVariables.settings_json.value[0]

        self.setWindowIcon(QIcon(self.resouces + '/wallman_icon.jpeg'))

        self.plotedImage = ""

        self.__adjustJsonVersion()
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
        self.ui.add_carousel.clicked.connect(self.__digit_newCarousel)
        self.ui.remove_carousel.clicked.connect(self.open_carouselList_widget)


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
        self.editCarouselName.emit(str(self.ui.carousel_select.currentText()))
        self.pathOperation.emit(pathOperationType.ADD,self.__get_folder())

    @Slot()
    def get_add_files(self):
        self.editCarouselName.emit(str(self.ui.carousel_select.currentText()))
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
        self.editCarouselName.emit(str(self.ui.carousel_select.currentText()))
        self.filesOperation.emit(pathOperationType.REMOVE,[path])

    @Slot()
    def get_remove_all_images(self):
        settings = {}
        with open(self.currentSettingsFile, 'r') as file:
            settings = json.load(file)

        self.closeWorker.emit()

        self.editCarouselName.emit(str(self.ui.carousel_select.currentText()))
        self.filesOperation.emit(pathOperationType.REMOVE,settings[settings['current_carousel']])

    @Slot()
    def open_imageList_widget(self):
        if self.imageList_widget is None or not self.imageList_widget.isVisible():
            self.imageList_widget = imageList_Widget(self.ui.carousel_select.currentText())
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

    def __digit_newCarousel(self):
        text, ok = QInputDialog.getText(self,"Wallman","Carousel name")
        if ok:
            settings = []
            with open(self.currentSettingsFile,'r') as file:
                settings = json.load(file)

            settings['carousel_list'].append(text)
            settings[str(text)] = []

            with open(self.currentSettingsFile,'w') as file:
                json.dump(settings,file,indent=4)

            self.ui.carousel_select.addItem(text)
            self.ui.carousel_select.setCurrentText(text)

    @Slot()
    def open_carouselList_widget(self):
        if self.carouselList_widget is None or not self.carouselList_widget.isVisible():
            self.carouselList_widget = carouselList_Widget()
            self.carouselList_widget.remove_carousel_request.connect(self.get_remove_carousel)
            self.carouselList_widget.show()

    @Slot(str)
    def get_remove_carousel(self,carousel):

        settings = {}
        with open(self.currentSettingsFile,'r') as file:
            settings = json.load(file)

        new_list = list(set(settings['carousel_list']) - set(carousel))
        settings['carousel_list'] = new_list

        settings.pop(carousel,None)

        with open(self.currentSettingsFile,'w') as file:
            json.dump(settings,file,indent=4)

    def __adjustJsonVersion(self):
        with open(self.settingsFile, 'r') as file:
            settings = json.load(file)

        if settings['version'] == 1.0:
            settings['version'] = 2.0
            settings['current_carousel'] = 'standard carousel'
            settings['carousel_list'] = ['standard carousel']
            settings['standard carousel'] = settings['images_list']
            del settings['images_list']

        with open(self.settingsFile,'w') as file:
            json.dump(settings,file,indent=4)

        with open(self.currentSettingsFile,'w') as file:
            json.dump(settings,file,indent=4)

    def __readCurrentSettings(self):
        with open(self.currentSettingsFile,'r') as file:
            settings = json.load(file)

        self.ui.time_edit.setText(str(settings['time']))
        self.ui.time_unit_box.setCurrentText(settings['time_unit'])
        self.ui.ui_system_box.setCurrentText(settings['ui_system'])
        self.ui.random_checkBox.setChecked(settings['random_display'])

        for carousel in settings['carousel_list']:
            self.ui.carousel_select.addItem(carousel)

    def __setIcons(self,object,resource):
        icon = QIcon(resource)
        object.setIcon(icon)
        object.setText('')

    def __getConfigs(self):
        configDict = {
            'time': int(self.ui.time_edit.toPlainText()),
            'time_unit': self.ui.time_unit_box.currentText(),
            'ui_system': self.ui.ui_system_box.currentText(),
            'random_display': self.ui.random_checkBox.isChecked(),
            'current_carousel': self.ui.carousel_select.currentText()
        }
        return configDict
