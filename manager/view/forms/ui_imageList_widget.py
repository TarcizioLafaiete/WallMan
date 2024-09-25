# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageList_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_imageListWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 400)
        self.imageList = QListWidget(Form)
        self.imageList.setObjectName(u"imageList")
        self.imageList.setGeometry(QRect(20, 10, 141, 31))
        self.ImageLabel = QLabel(Form)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setGeometry(QRect(330, 110, 250, 200))
        self.RemoveButton = QPushButton(Form)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setGeometry(QRect(390, 360, 89, 25))
        self.CloseButtton = QPushButton(Form)
        self.CloseButtton.setObjectName(u"CloseButtton")
        self.CloseButtton.setGeometry(QRect(490, 360, 89, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ImageLabel.setText("")
        self.RemoveButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.CloseButtton.setText(QCoreApplication.translate("Form", u"Close", None))
    # retranslateUi

