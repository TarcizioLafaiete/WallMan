from PySide6.QtWidgets import QWidget,QListWidget
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Signal,Slot

from .forms.ui_imageList_widget import Ui_imageListWidget
from business.utils import envorimentVariables

import json

class carouselList_Widget(QWidget):

    remove_carousel_request = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_imageListWidget()
        self.ui.setupUi(self)

        self.ui.RemoveButton.setVisible(False)
        self.ui.removeAllButton.setStyleSheet("background-color: #AA0000")
        self.ui.removeAllButton.setText("Remove")

        self.connectSignalsAndSlots()

        self.currentSettingsFile = envorimentVariables.current_settings_json.value[0]
        self.carouselList = []
        self.currentCarousel = ""

        self.__listCarousels()

    def connectSignalsAndSlots(self):
        self.ui.removeAllButton.clicked.connect(self.removeCarousel)
        self.ui.imageList.itemClicked.connect(self.__getCurrentCarousel)

    def removeCarousel(self):
        self.remove_carousel_request.emit(self.currentCarousel)
        self.ui.imageList.clear()
        self.__listCarousels()

    def __getCurrentCarousel(self,item):
        self.currentCarousel = item.text()
        print(f"Nome do carousel: {self.currentCarousel}")

    def __listCarousels(self):
        
        with open(self.currentSettingsFile,'r') as file:
            settings = json.load(file)
            self.carouselList = settings["carousel_list"]

        self.ui.imageList.setFixedWidth(235)

        row_height = self.ui.imageList.sizeHintForRow(0)
        num_carousels = len(self.carouselList)
        new_height = row_height * num_carousels+2 * self.ui.imageList.frameWidth()
        self.ui.imageList.setFixedHeight(max(min(new_height,300),350))

        self.ui.imageList.addItems(self.carouselList)