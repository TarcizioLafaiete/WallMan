import sys
from PySide6.QtWidgets import QApplication,QWidget
from view.mainwindow import mainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()
    sys.exit(app.exec())