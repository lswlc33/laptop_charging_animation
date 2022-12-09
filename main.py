from Ui_animation import *
import sys,time, psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtCore import QTimer
a = psutil.sensors_battery()
old_battery = a.power_plugged
battery = a.power_plugged

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
        # 文字定位安放
        self.text_loca()
        

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

    def text_loca(self):
        xx, yy = 670, 490
        ay, ax = self.get_screen_size()
        ax = ax/2 - xx/2 + 200
        ay = ay/2 - yy/2 - 165
        self.label_2.setGeometry(ax, ay, xx, yy)

    def init_timer(self):
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.if_changed)
        self.timer2.start(500)


    def if_changed(self):
        global battery , old_battery
        a = psutil.sensors_battery()
        battery = a.power_plugged
        print(battery)
        if old_battery == battery:
            print(0)
        elif old_battery != battery:
            if battery:
                print("开始充电啦!")
                self.label_2.setText("开始充电啦!")
                self.init_window()
            elif not battery:
                self.label_2.setText("断开电源啦!")
                print("断开电源啦!")
                self.init_window()
            old_battery = battery
    
        
            
            
    def init_window(self):
        self.show()
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.hide_an)
        self.timer1.start(1500)
        

    def hide_an(self):
        self.hide()
        self.timer1.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = animation()
    a.init_timer()
    sys.exit(app.exec_())

