# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import gpiod


# La clase generada por Qt Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(10, 420, 150, 150))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo_ecci2.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.students_label = QtWidgets.QLabel(self.centralwidget)
        self.students_label.setGeometry(QtCore.QRect(160, 420, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.students_label.setFont(font)
        self.students_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.students_label.setObjectName("students_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 165, 280, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.status_label.setFont(font)
        self.status_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.status_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("status_label")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Lectura Pin Digital"))
        self.students_label.setText(
            _translate(
                "MainWindow",
                "Cristian Villamil\n"
                "David Rodriguez\n"
                "Johant Piracoca\n"
                "Laura Valiente",
            )
        )
        self.status_label.setText(_translate("MainWindow", "TextLabel"))


# Nueva clase para manejar la lógica de la GUI
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Crear una instancia de la UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configuración del temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_button)
        self.timer.start(100)  # Verifica el estado del botón cada 100 ms

        # Configuración del botón físico
        self.BUTTON_PIN = 27
        self.chip = gpiod.Chip("gpiochip4")
        self.button_line = self.chip.get_line(self.BUTTON_PIN)
        self.button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

    def check_button(self):
        # Leer el estado del botón (1 presionado, 0 no presionado)
        self.button_state = self.button_line.get_value()
        if self.button_state == 1:
            self.ui.status_label.setText("alto")
            self.ui.status_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.ui.status_label.setText("bajo")
            self.ui.status_label.setStyleSheet("background-color: rgb(0, 85, 255);")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()  # Instancia de la nueva clase MainWindow
    window.show()
    sys.exit(app.exec_())
