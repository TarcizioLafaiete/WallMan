#!/bin/python3

import sys
from PySide6.QtWidgets import QApplication,QWidget
from view.mainwindow import mainWindow
from control.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    controller = Controller(window)
    window.show()
    sys.exit(app.exec())