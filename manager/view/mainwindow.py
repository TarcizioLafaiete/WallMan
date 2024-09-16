from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from .forms.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Signal,Slot
import json

class mainWindow(QMainWindow):

    startWorker = Signal(dict)
    closeWorker = Signal()
    saveConfig = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__readCurrentSettings()
        self.connectSignalsAndSlots()
        self.ui.start_button.setStyleSheet("background-color: #00AA00")
        self.ui.close_button.setStyleSheet("background-color: #AA0000")

        self.__setIcons(self.ui.newImages_folder,'view/forms/resources/adicionar-pasta.png')
        self.__setIcons(self.ui.ignoreImages_folder,'view/forms/resources/adicionar-pasta.png')
        self.__setIcons(self.ui.nsfw_folder,'view/forms/resources/adicionar-pasta.png')

        self.__setIcons(self.ui.newImages_files,'view/forms/resources/adicionar-imagem.png')
        self.__setIcons(self.ui.ignoreImages_files,'view/forms/resources/adicionar-imagem.png')
        self.__setIcons(self.ui.nsfw_files,'view/forms/resources/adicionar-imagem.png')


    def connectSignalsAndSlots(self):
        self.ui.start_button.clicked.connect(self.start_button_clicked)
        self.ui.close_button.clicked.connect(self.close_button_clicked)
        self.ui.save_button.clicked.connect(self.saveConfig_button_clicked)

    @Slot()
    def start_button_clicked(self):
        configDict = {
            'time': int(self.ui.time_edit.toPlainText()),
            'time_unit': self.ui.time_unit_box.currentText(),
            'ui_system': self.ui.ui_system_box.currentText(),
            'ignore_images': self.ui.ignore_checkBox.isChecked(),
            'random_display': self.ui.random_checkBox.isChecked(),
            'mature_content': self.ui.nsfw_checkBox.isChecked()
        }
        self.startWorker.emit(configDict)

    @Slot()
    def close_button_clicked(self):
        self.closeWorker.emit()

    @Slot()
    def saveConfig_button_clicked(self):
        self.saveConfig.emit()
    
    # @Slot()
    # def get_folder(self):


    def __readCurrentSettings(self):
        with open('../settings.json','r') as file:
            settings = json.load(file)

        self.ui.time_edit.setText(str(settings['time']))
        self.ui.time_unit_box.setCurrentText(settings['time_unit'])
        self.ui.ui_system_box.setCurrentText(settings['ui_system'])

        self.ui.ignore_checkBox.setChecked(settings['ignore_images'])
        self.ui.random_checkBox.setChecked(settings['random_display'])
        self.ui.nsfw_checkBox.setChecked(settings['mature_content'])

        with open('../currentSettings.json','w') as file:
            json.dump(settings,file,indent=4)

    def __setIcons(self,object,resource):
        icon = QIcon(resource)
        object.setIcon(icon)
        object.setText('')