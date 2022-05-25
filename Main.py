import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import GUI.MainGUI
import Handle
class MainClass(QMainWindow, GUI.MainGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        Handle.Handle(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = MainClass()
    myWindow.show()
    app.exec_()