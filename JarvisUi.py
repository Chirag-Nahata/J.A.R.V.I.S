from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-20, -50, 1681, 851))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("G.U.I Material\\B.G\\Black_Template.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1000, 480, 361, 51))
        self.textBrowser_2.setStyleSheet("background-color: Transparent;\n"
"color: rgb(85, 255, 255);\n"
"font:28px")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 451, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("G.U.I Material\\B.G\\Iron_Template_1.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(10, 10, 471, 301))
        self.bg_2.setStyleSheet("color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 255, 255);")
        self.bg_2.setText("")
        self.bg_2.setPixmap(QtGui.QPixmap("G.U.I Material/B.G/wdwdwd.png"))
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 20, 491, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("G.U.I Material\\ExtraGui\\live.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 10, 511, 301))
        self.label_5.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-280, 150, 941, 631))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("G.U.I Material\\VoiceReg\\__1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1000, 420, 361, 51))
        self.textBrowser_3.setStyleSheet("background-color: Transparent;\n"
"color: rgb(85, 255, 255);\n"
"font:28px")
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 370, 151, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1190, 370, 161, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 30, 131, 41))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1220, 30, 131, 41))
        self.pushButton_4.setStyleSheet("\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);\n")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1070, 90, 131, 41))
        self.pushButton_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5") 

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1220, 90, 131, 41))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.bg_9 = QtWidgets.QLabel(self.centralwidget)
        self.bg_9.setGeometry(QtCore.QRect(-20, 260, 471, 461))
        self.bg_9.setText("")
        self.bg_9.setPixmap(QtGui.QPixmap("G.U.I Material//B.G//wdwdwd.png"))
        self.bg_9.setScaledContents(True)
        self.bg_9.setObjectName("bg_9")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1070, 150, 281, 191))
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1080, 160, 261, 171))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("G.U.I Material\\ExtraGui\\Earth.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.bg.raise_()
        self.label_2.raise_()
        self.textBrowser_2.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.bg_2.raise_()
        self.label.raise_()
        self.textBrowser_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.bg_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "START"))

        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))

        self.pushButton_3.setText(_translate("MainWindow", "YouTube"))

        self.pushButton_4.setText(_translate("MainWindow", "Whatsapp"))

        self.pushButton_5.setText(_translate("MainWindow", "Chrome"))

        self.pushButton_6.setText(_translate("MainWindow", "Vs Code"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
