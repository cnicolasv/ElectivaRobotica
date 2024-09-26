
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from adafruit_servokit import ServoKit


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(341, 574)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.motor_angle = QtWidgets.QLabel(self.centralwidget)
        self.motor_angle.setGeometry(QtCore.QRect(40, 30, 260, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.motor_angle.setFont(font)
        self.motor_angle.setFrameShape(QtWidgets.QFrame.Box)
        self.motor_angle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.motor_angle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.motor_angle.setObjectName("motor_angle")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 320, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.motor_slider = QtWidgets.QSlider(self.centralwidget)
        self.motor_slider.setGeometry(QtCore.QRect(40, 210, 260, 41))
        self.motor_slider.setMaximum(180)
        self.motor_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.motor_slider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.motor_slider.setObjectName("motor_slider")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(10, 400, 150, 150))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo_ecci2.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.students_label = QtWidgets.QLabel(self.centralwidget)
        self.students_label.setGeometry(QtCore.QRect(190, 400, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.students_label.setFont(font)
        self.students_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.students_label.setObjectName("students_label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        self.motor_slider.valueChanged.connect(self.set_angle)
        self.lineEdit.editingFinished.connect(self.set_angle)

        self.motor = "motor 1"
        self.motor_angle.setText(self.motor)

        self.kit = ServoKit(channels=16)

    def set_angle(self):
        
        #angle = self.motor_slider.value()
        self.motor = self.lineEdit.text()
        self.motor = self.motor.strip().lower()
        if self.motor == "motor 1":
                angle1 = self.motor_slider.value()
                self.kit.servo[0].angle = angle1
        elif self.motor == "motor 2":
                angle2 = self.motor_slider.value()
                self.kit.servo[1].angle = angle2
        else:
                self.motor_angle.setText("Select a Motor")
        
        
        #self.motor_angle.setText(str(self.motor))
        

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Control de Motores"))
        self.motor_angle.setText(_translate("mainWindow", "TextLabel"))
        self.students_label.setText(_translate("mainWindow", "Cristian Villamil\n"
"Laura Valiente\n"
"David Rodriguez\n"
"Johant Piracoca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
