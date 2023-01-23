######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_ihackyou6( QtWidgets.QMainWindow ):
    def __init__(self): #*****
        super().__init__() #*****

        self.setupUi() #*****  

    def setupUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")
        self.setWindowTitle("")
        self.resize(384, 267)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(-10, -10, 401, 281))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("./image/icon.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
