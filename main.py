from Ui_animation import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class animation(QMainWindow, Ui_animation):
    def __init__(self, parent=None):
        super(animation, self).__init__(parent)
        self.setupUi(self)
        # 设置全屏
        self.set_screen_size()
        # 窗口透明和无边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # 图片定位安放
        self.pic_loca()
        self.init_timer()

    def get_screen_size(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        return self.height, self.width

    def set_screen_size(self):
        height, width = self.get_screen_size()
        self.setFixedSize(width, height)

    def pic_loca(self):
        xx, yy = 670, 490
        ay, ax = self.get_screen_size()
        ax = ax/2 - xx/2
        ay = ay/2 - yy/2
        self.label.setGeometry(ax, ay, xx, yy)

    def init_timer(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.if_changed)
        timer.start(500)

    def if_changed(self):

        if input() == "1":
            self.init_window()
            
    def init_window(self):
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = animation()
    sys.exit(app.exec_())

