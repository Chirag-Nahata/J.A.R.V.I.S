from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import webbrowser as web
import sys
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
import Main
from JarvisUi import Ui_MainWindow

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.BestVer()
          
startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.jarvis_ui = Ui_MainWindow()
        
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

        self.jarvis_ui.pushButton_3.clicked.connect(self.YouTubeButton)

        self.jarvis_ui.pushButton_6.clicked.connect(self.VsCode)

        self.jarvis_ui.pushButton_4.clicked.connect(self.WhatsappButton)

        self.jarvis_ui.pushButton_5.clicked.connect(self.ChromeButtom)

    def YouTubeButton(self):
        web.open("https://www.youtube.com/")

    def ChromeButtom(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def WhatsappButton(self):
        web.open("https://web.whatsapp.com/")

    def VsCode(self):
        os.startfile("E:\\Kaushik Shresth\\Applications\\Microsoft VS Code\\Code.exe")

    def startFunc(self):

        self.jarvis_ui.movies_2 = QtGui.QMovie("G.U.I Material\\VoiceReg\\__1.gif")

        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_2)

        self.jarvis_ui.movies_2.start()


        self.jarvis_ui.movies_3 = QtGui.QMovie("G.U.I Material\\ExtraGui\\live.gif")

        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)

        self.jarvis_ui.movies_3.start()


        self.jarvis_ui.movies_5 = QtGui.QMovie("G.U.I Material\\B.G\\Iron_Template_1.gif")

        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies_5)

        self.jarvis_ui.movies_5.start()

        self.jarvis_ui.movie = QtGui.QMovie("G.U.I Material\\ExtraGui\\Earth.gif")

        self.jarvis_ui.label_7.setMovie(self.jarvis_ui.movie)

        self.jarvis_ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunctions.start()

    def showtime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        labbel = " Time Is Now :  " + label_time 
        label_date = now.toString(Qt.ISODate)
        labdsbdh = " Today's Date : " + label_date
        self.jarvis_ui.textBrowser_3.setText(labbel)
        self.jarvis_ui.textBrowser_2.setText(labdsbdh)

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
