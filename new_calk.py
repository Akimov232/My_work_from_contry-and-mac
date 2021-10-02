from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(311, 302)
        mainwindow.setMinimumSize(QtCore.QSize(311, 302))
        mainwindow.setMaximumSize(QtCore.QSize(311, 302))
        mainwindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mainwindow.setMouseTracking(False)
        mainwindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 311, 31))
        self.label.setMaximumSize(QtCore.QSize(700, 700))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 241, 111, 61))
        self.btn_0.setMaximumSize(QtCore.QSize(8888888, 888888))
        self.btn_0.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_0.setDefault(False)
        self.btn_0.setObjectName("btn_0")
        self.btn_equel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equel.setGeometry(QtCore.QRect(111, 241, 129, 61))
        self.btn_equel.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_equel.setObjectName("btn_equel")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 171, 80, 70))
        self.btn_1.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 101, 80, 70))
        self.btn_4.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 31, 80, 70))
        self.btn_7.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 31, 80, 70))
        self.btn_8.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 101, 80, 70))
        self.btn_5.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 171, 80, 70))
        self.btn_2.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(160, 31, 80, 70))
        self.btn_9.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(160, 101, 80, 70))
        self.btn_6.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(160, 171, 80, 70))
        self.btn_3.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(240, 31, 71, 70))
        self.btn_plus.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_plus.setObjectName("btn_plus")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 101, 71, 70))
        self.pushButton.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 171, 71, 70))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 241, 71, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 205, 102);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        self.calk_move()
        
        self.is_equl = False

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("funny calk", "funny calk"))
        self.label.setText(_translate("mainwindow", "0"))
        self.btn_0.setText(_translate("mainwindow", "0"))
        self.btn_equel.setText(_translate("mainwindow", "="))
        self.btn_1.setText(_translate("mainwindow", "1"))
        self.btn_4.setText(_translate("mainwindow", "4"))
        self.btn_7.setText(_translate("mainwindow", "7"))
        self.btn_8.setText(_translate("mainwindow", "8"))
        self.btn_5.setText(_translate("mainwindow", "5"))
        self.btn_2.setText(_translate("mainwindow", "2"))
        self.btn_9.setText(_translate("mainwindow", "9"))
        self.btn_6.setText(_translate("mainwindow", "6"))
        self.btn_3.setToolTip(_translate("mainwindow", "<html><head/><body><p>1</p></body></html>"))
        self.btn_3.setText(_translate("mainwindow", "3"))
        self.btn_plus.setText(_translate("mainwindow", "+"))
        self.pushButton.setText(_translate("mainwindow", "-"))
        self.pushButton_2.setText(_translate("mainwindow", "*"))
        self.pushButton_3.setText(_translate("mainwindow", "/"))
        
    def calk_move(self):
            self.btn_0.clicked.connect(lambda:self.write_number(self.btn_0.text()))
            self.btn_1.clicked.connect(lambda:self.write_number(self.btn_1.text()))
            self.btn_2.clicked.connect(lambda:self.write_number(self.btn_2.text()))
            self.btn_3.clicked.connect(lambda:self.write_number(self.btn_3.text()))
            self.btn_4.clicked.connect(lambda:self.write_number(self.btn_4.text()))
            self.btn_5.clicked.connect(lambda:self.write_number(self.btn_5.text()))
            self.btn_6.clicked.connect(lambda:self.write_number(self.btn_6.text()))
            self.btn_7.clicked.connect(lambda:self.write_number(self.btn_7.text()))
            self.btn_8.clicked.connect(lambda:self.write_number(self.btn_8.text()))
            self.btn_9.clicked.connect(lambda:self.write_number(self.btn_9.text()))
            self.btn_plus.clicked.connect(lambda:self.write_number(self.btn_plus.text()))
            self.pushButton.clicked.connect(lambda:self.write_number(self.pushButton.text()))
            self.pushButton_2.clicked.connect(lambda:self.write_number(self.pushButton_2.text()))
            self.pushButton_3.clicked.connect(lambda:self.write_number(self.pushButton_3.text()))
            self.btn_equel.clicked.connect(self.resalts)
            
    
    def write_number(self , number):
            if self.label.text() == "0" or self.is_equl:
                self.label.setText(number)
                self.is_equl = False
            else:
                self.label.setText(self.label.text() +number)
                    
    def resalts(self):
            if not self.is_equl:
                res = eval(self.label.text())
                self.label.setText(str(res))
                self.is_equl = True
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Сейчас это сделать нельзя")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                
                error.exec_()
                
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
