from Ui_animation import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class animation(QMainWindow, Ui_animation):
    def __init__(self, parent=None):
        super(animation, self).__init__(parent)
        self.setupUi(self)
        self.geometry()

    def get_geometry(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = animation()
    myWin.show()
    sys.exit(app.exec_())