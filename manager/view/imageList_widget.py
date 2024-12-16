from PySide6.QtWidgets import QWidget,QListWidget
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Signal,Slot

from .forms.ui_imageList_widget import Ui_imageListWidget
from business.utils import pathOperationType,envorimentVariables

import cv2
import json

class imageList_Widget(QWidget):

    remove_image_request = Signal(str)
    remove_all_images_request = Signal()

    def __init__(self,carouselName:str):
        super().__init__()
        self.ui = Ui_imageListWidget()
        self.ui.setupUi(self)

        self.ui.removeAllButton.setStyleSheet("background-color: #AA0000");

        self.connectSignalsAndSlots()

        self.currentSettingsFile = envorimentVariables.current_settings_json.value[0]

        self.carouselName = carouselName
        self.imageList = []
        self.currentImage = ""

        self.__listImages()

    def connectSignalsAndSlots(self):
        self.ui.imageList.itemClicked.connect(self.plot_image)
        self.ui.RemoveButton.clicked.connect(self.remove_image)
        self.ui.removeAllButton.clicked.connect(self.remove_all_images)

    def plot_image(self,item):

        for img in self.imageList:
            if img.find(item.text()) >= 0:
                self.currentImage = img
                break
        
        image = cv2.imread(self.currentImage)
        miniature = cv2.resize(image,(300,200))

        rgb_miniature = cv2.cvtColor(miniature,cv2.COLOR_BGR2RGB)
        h,w,ch = rgb_miniature.shape

        bytes_per_line = ch * w
        q_image = QImage(rgb_miniature.data,w,h,bytes_per_line,QImage.Format.Format_RGB888)
        q_pixmap = QPixmap.fromImage(q_image)

        self.ui.ImageLabel.setPixmap(q_pixmap)

    @Slot()
    def remove_image(self):
        self.remove_image_request.emit(self.currentImage)
        self.ui.imageList.clear()
        self.__listImages()

    @Slot()
    def remove_all_images(self):
        self.ui.imageList.clear()
        self.remove_all_images_request.emit()    

    def __listImages(self):
    
        with open(self.currentSettingsFile,'r') as file:
            settings = json.load(file)
            self.imageList = settings[self.carouselName]

        self.ui.imageList.setFixedWidth(235)

        row_height = self.ui.imageList.sizeHintForRow(0)
        num_files = len(self.imageList)
        new_height = row_height * num_files+2 * self.ui.imageList.frameWidth()
        self.ui.imageList.setFixedHeight(max(min(new_height,300),350))

        self.ui.imageList.addItems(self.__getImageName(self.imageList))

    def __getImageName(self,imageList:list[str]) -> list:
        name_list = []

        for image in imageList:
            name_list.append(image.split('/')[-1])
        
        return self.__normImageNames(name_list)
    
    def __normImageNames(self,names:list[str]) -> list:

        supper_names = {}
        lower_names = {}

        for name in names:
            check = False
            if any(letter.isupper() for letter in name):
                check = True
                supper_names.update({name.lower() : name})
            lower_names.update({name.lower() : check})

        
        sorted_names = sorted(list(lower_names.keys()))
        return [supper_names[name] if lower_names[name] else name for name in sorted_names]
            