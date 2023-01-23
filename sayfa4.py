from PyQt5 import QtCore, QtGui, QtWidgets
from sayfa5 import Ui_ihackyou5
from sayfa6 import Ui_ihackyou6

class Ui_ihackyou4( QtWidgets.QMainWindow ):
    def __init__(self): #*****
        super().__init__() #*****

        self.setupUi() #*****  


    def sayfacagir(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ihackyou5()
        self.ui.show()
        self.close()        

    def sayfacagir2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ihackyou6()
        self.ui.show()
        self.close()        



    def setupUi(self):
        self.setObjectName("ihackyou")
        self.resize(341, 195)
        self.setWindowTitle(" I LOVE YOU <3 ")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(100, 40, 211, 61))
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
        self.evet.setGeometry(QtCore.QRect(60, 150, 101, 31))
        self.evet.setStyleSheet("border: 1px solid #3A3939;")
        self.evet.setObjectName("evet")
        self.warningicon = QtWidgets.QLabel(self.centralwidget)
        self.warningicon.setGeometry(QtCore.QRect(20, 40, 61, 61))
        self.warningicon.setText("")
        self.warningicon.setPixmap(QtGui.QPixmap("./image/war.png"))
        self.warningicon.setScaledContents(True)
        self.warningicon.setObjectName("warningicon")
        self.hayir = QtWidgets.QPushButton(self.centralwidget)
        self.hayir.setGeometry(QtCore.QRect(180, 150, 101, 31))
        self.hayir.setStyleSheet("border: 1px solid #3A3939;")
        self.hayir.setObjectName("hayir")
        self.setCentralWidget(self.centralwidget)

        self.hayir.clicked.connect(self.sayfacagir)
        self.evet.clicked.connect(self.sayfacagir2)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.text1.setText(_translate("ihackyou", "Lütfen !"))
        self.evet.setText(_translate("ihackyou", "Evet"))
        self.hayir.setText(_translate("ihackyou", "Hayır"))
