# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\OneDrive\python\laptop_charging_animation\animation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_animation(object):
    def setupUi(self, animation):
        animation.setObjectName("animation")
        animation.resize(902, 626)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(animation.sizePolicy().hasHeightForWidth())
        animation.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(animation)
        self.label.setGeometry(QtCore.QRect(110, 150, 670, 490))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/res/img1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(animation)
        self.label_2.setGeometry(QtCore.QRect(250, 190, 281, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(animation)
        QtCore.QMetaObject.connectSlotsByName(animation)

    def retranslateUi(self, animation):
        _translate = QtCore.QCoreApplication.translate
        animation.setWindowTitle(_translate("animation", "animation"))
        self.label_2.setText(_translate("animation", "电源模式！"))
import res_rc
