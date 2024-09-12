# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(222, 221, 218, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(238, 238, 236, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(111, 110, 109, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(148, 147, 145, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(111, 110, 109, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 771, 141))
        self.time_edit = QTextEdit(self.groupBox)
        self.time_edit.setObjectName(u"time_edit")
        self.time_edit.setGeometry(QRect(60, 40, 71, 21))
        self.timer_label = QLabel(self.groupBox)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setGeometry(QRect(20, 40, 67, 17))
        self.time_unit_box = QComboBox(self.groupBox)
        self.time_unit_box.addItem("")
        self.time_unit_box.addItem("")
        self.time_unit_box.addItem("")
        self.time_unit_box.addItem("")
        self.time_unit_box.setObjectName(u"time_unit_box")
        self.time_unit_box.setGeometry(QRect(140, 40, 86, 21))
        self.ui_system_label = QLabel(self.groupBox)
        self.ui_system_label.setObjectName(u"ui_system_label")
        self.ui_system_label.setGeometry(QRect(420, 40, 81, 17))
        self.ui_system_box = QComboBox(self.groupBox)
        self.ui_system_box.addItem("")
        self.ui_system_box.addItem("")
        self.ui_system_box.setObjectName(u"ui_system_box")
        self.ui_system_box.setGeometry(QRect(500, 40, 86, 21))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 90, 711, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ignore_checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.ignore_checkBox.setObjectName(u"ignore_checkBox")

        self.horizontalLayout.addWidget(self.ignore_checkBox)

        self.random_checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.random_checkBox.setObjectName(u"random_checkBox")

        self.horizontalLayout.addWidget(self.random_checkBox)

        self.nsfw_checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.nsfw_checkBox.setObjectName(u"nsfw_checkBox")

        self.horizontalLayout.addWidget(self.nsfw_checkBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 190, 331, 261))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 50, 291, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mature_toolButton = QToolButton(self.gridLayoutWidget)
        self.mature_toolButton.setObjectName(u"mature_toolButton")

        self.gridLayout.addWidget(self.mature_toolButton, 2, 1, 1, 1)

        self.newImages_toolButton = QToolButton(self.gridLayoutWidget)
        self.newImages_toolButton.setObjectName(u"newImages_toolButton")

        self.gridLayout.addWidget(self.newImages_toolButton, 0, 1, 1, 1)

        self.ignore_toolButton = QToolButton(self.gridLayoutWidget)
        self.ignore_toolButton.setObjectName(u"ignore_toolButton")

        self.gridLayout.addWidget(self.ignore_toolButton, 1, 1, 1, 1)

        self.new_images_label = QLabel(self.gridLayoutWidget)
        self.new_images_label.setObjectName(u"new_images_label")

        self.gridLayout.addWidget(self.new_images_label, 0, 0, 1, 1)

        self.ignore_label = QLabel(self.gridLayoutWidget)
        self.ignore_label.setObjectName(u"ignore_label")

        self.gridLayout.addWidget(self.ignore_label, 1, 0, 1, 1)

        self.mature_label = QLabel(self.gridLayoutWidget)
        self.mature_label.setObjectName(u"mature_label")

        self.gridLayout.addWidget(self.mature_label, 2, 0, 1, 1)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(450, 510, 101, 31))
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(560, 510, 101, 31))
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(670, 510, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuWallMan_Program = QMenu(self.menubar)
        self.menuWallMan_Program.setObjectName(u"menuWallMan_Program")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWallMan_Program.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Configurations", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.time_unit_box.setItemText(0, QCoreApplication.translate("MainWindow", u"sec", None))
        self.time_unit_box.setItemText(1, QCoreApplication.translate("MainWindow", u"min", None))
        self.time_unit_box.setItemText(2, QCoreApplication.translate("MainWindow", u"hour", None))
        self.time_unit_box.setItemText(3, QCoreApplication.translate("MainWindow", u"day", None))

        self.ui_system_label.setText(QCoreApplication.translate("MainWindow", u"Ui System:", None))
        self.ui_system_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Gnome", None))
        self.ui_system_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Kde", None))

        self.ignore_checkBox.setText(QCoreApplication.translate("MainWindow", u"Use ignore list images setting", None))
        self.random_checkBox.setText(QCoreApplication.translate("MainWindow", u"Randomize display images", None))
        self.nsfw_checkBox.setText(QCoreApplication.translate("MainWindow", u"Block not safe to work images", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Wallpapers Manipulation", None))
        self.mature_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.newImages_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ignore_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.new_images_label.setText(QCoreApplication.translate("MainWindow", u"Add new Images", None))
        self.ignore_label.setText(QCoreApplication.translate("MainWindow", u"Add Image to ignore list", None))
        self.mature_label.setText(QCoreApplication.translate("MainWindow", u"Add image to mature content list", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuWallMan_Program.setTitle(QCoreApplication.translate("MainWindow", u"WallMan Program", None))
    # retranslateUi

