
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainWindow_5
import sqlite3
import sys

class Ui_MainWindow(object):

    def messagebox(self, title, msg):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(msg)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def openWindowLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_5()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def openLogin(self):
        self.openWindowLogin()

    def showdocCombobox(self):
        self.con = sqlite3.connect("hms.db")
        self.cur = self.con.cursor()

        self.cur.execute('''SELECT docname FROM doc''')
        data = self.cur.fetchall()
        for doc in data:
            self.cbdochome.addItem(doc[0])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(280, 20, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(36)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(200, 14, 79);")
        self.label_title.setObjectName("label_title")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 120, 751, 461))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.cbdochome = QtWidgets.QComboBox(self.tabWidgetPage1)
        self.cbdochome.setGeometry(QtCore.QRect(150, 160, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cbdochome.setFont(font)
        self.cbdochome.setStyleSheet("")
        self.cbdochome.setObjectName("cbdochome")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_5.setGeometry(QtCore.QRect(50, 250, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.homespec = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.homespec.setGeometry(QtCore.QRect(150, 210, 113, 20))
        self.homespec.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.homespec.setReadOnly(True)
        self.homespec.setObjectName("homespec")
        self.homequal = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.homequal.setGeometry(QtCore.QRect(150, 250, 113, 20))
        self.homequal.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.homequal.setAutoFillBackground(False)
        self.homequal.setReadOnly(True)
        self.homequal.setObjectName("homequal")
        self.label_6 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.tabWidgetPage1)
        self.line.setGeometry(QtCore.QRect(320, 70, 20, 371))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LoginMain = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.LoginMain.setGeometry(QtCore.QRect(460, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.LoginMain.setFont(font)
        self.LoginMain.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.LoginMain.setObjectName("LoginMain")
        self.LoginMain.clicked.connect(self.openLogin)
        self.label_7 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_7.setGeometry(QtCore.QRect(360, 160, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tabWidgetPage2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.label = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label.setGeometry(QtCore.QRect(20, 40, 711, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.tabWidgetPage3)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 751, 441))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "My HeathCare"))
        self.label_2.setText(_translate("MainWindow", "Doctor Name :"))
        self.label_3.setText(_translate("MainWindow", "Welcome to My HealthCare "))
        self.label_4.setText(_translate("MainWindow", "Specialiation :"))
        self.label_5.setText(_translate("MainWindow", "Qualification :"))
        self.label_6.setText(_translate("MainWindow", "Select doctor to see information"))
        self.LoginMain.setText(_translate("MainWindow", "Login"))
        self.label_7.setText(_translate("MainWindow", "To Login or Register click the following button"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Home"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">About Us </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">MyHealthcare is dedicated to helping people live healthier lives and making the health system work better for everyone. We serve millions of people from their earliest years through their working lives and through retirement.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "About"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600; background-color:#ffffff;\">Answering your questions is central to our mission: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; background-color:#ffffff;\">We launched the new HealthCare.gov to feature an easy-to-understand question and answer format, with content based on the most common questions we hear from you. </span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">We provided you with new way get your health insurance options and info—just answer a few quick questions and we’ll provide you with a personalized list of coverage options, content tailored to your situation, and a checklist to help you get ready. </span></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; background-color:#ffffff;\">Get help when you need it Call us right now to get your Marketplace questions answered by a customer service representative, available 24/7:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; background-color:#ffffff;\"> </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; background-color:#ffffff;\">Phone no. : </span><a href=\"tel:999-999-9999\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff; background-color:#ffffff;\">99999 99999</span></a></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">E-mail : </span><a href=\"mailto:myhealthcare@xyz.com\"><span style=\" text-decoration: underline; color:#0000ff; background-color:#ffffff;\"> myhealthcare@xyz.com</span></a></li></ul></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Contact Us"))
        self.showdocCombobox()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
