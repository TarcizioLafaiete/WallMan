from PySide6.QtWidgets import QMainWindow
from .forms.ui_mainwindow import Ui_MainWindow
import json

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__readCurrentSettings()
        self.ui.start_button.setStyleSheet("background-color: #00AA00")
        self.ui.close_button.setStyleSheet("background-color: #AA0000")


    def __readCurrentSettings(self):
        with open('../settings.json','r') as file:
            settings = json.load(file)

        self.ui.time_edit.setText(str(settings['time']))
        self.ui.time_unit_box.setCurrentText(settings['time_unit'])
        self.ui.ui_system_box.setCurrentText(settings['ui_system'])

        self.ui.ignore_checkBox.setChecked(settings['ignore_images'])
        self.ui.random_checkBox.setChecked(settings['random_display'])
        self.ui.nsfw_checkBox.setChecked(settings['mature_content'])