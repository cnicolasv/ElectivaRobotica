# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.led1_slider = QtWidgets.QSlider(self.centralwidget)
        self.led1_slider.setGeometry(QtCore.QRect(60, 220, 41, 160))
        self.led1_slider.setStyleSheet("alternate-background-color: rgb(75, 255, 249);")
        self.led1_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.led1_slider.setObjectName("led1_slider")
        self.led2_slider = QtWidgets.QSlider(self.centralwidget)
        self.led2_slider.setGeometry(QtCore.QRect(210, 220, 41, 160))
        self.led2_slider.setStyleSheet("border-top-color: rgb(255, 85, 127);")
        self.led2_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.led2_slider.setObjectName("led2_slider")
        self.red_button = QtWidgets.QPushButton(self.centralwidget)
        self.red_button.setGeometry(QtCore.QRect(30, 110, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.red_button.setFont(font)
        self.red_button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.red_button.setObjectName("red_button")
        self.green_button = QtWidgets.QPushButton(self.centralwidget)
        self.green_button.setGeometry(QtCore.QRect(180, 110, 110, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.green_button.setFont(font)
        self.green_button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.green_button.setObjectName("green_button")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(10, 420, 150, 150))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo_ecci2.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.names_label = QtWidgets.QLabel(self.centralwidget)
        self.names_label.setGeometry(QtCore.QRect(160, 420, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.names_label.setFont(font)
        self.names_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.names_label.setObjectName("names_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SitBlock"))
        self.red_button.setText(_translate("MainWindow", "Red Led"))
        self.green_button.setText(_translate("MainWindow", "Green Led"))
        self.names_label.setText(_translate("MainWindow", "Cristian Villamil\n"
"David Rodriguez\n"
"Johant Piracoca\n"
"Laura Valiente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
