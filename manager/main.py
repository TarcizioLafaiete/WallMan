#!/bin/python3

import sys
import os
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QIcon
from view.mainwindow import mainWindow
from control.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(os.getenv("RESOURCES_DIR") + "/wallman_icon.jpeg"))
    window = mainWindow()
    controller = Controller(window)
    window.show()
    sys.exit(app.exec())
