import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 201, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 10, 211, 131))
        self.label_5.setStyleSheet("border-image: url(logo1.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 150, 221, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 201, 61))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 201, 61))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(100, 100, 201, 61))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(290, 500, 81, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(240, 470, 181, 31))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")

        self.Grafica = QtWidgets.QGraphicsView(self.centralwidget)
        self.Grafica.setGeometry(QtCore.QRect(370, 220, 271, 201))
        self.Grafica.setObjectName("Grafica")
        self.scene = QGraphicsScene()
        self.Grafica.setScene(self.scene)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 210, 141, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 190, 141, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.Resistencia = QtWidgets.QSlider(self.centralwidget)
        self.Resistencia.setGeometry(QtCore.QRect(70, 240, 171, 21))
        self.Resistencia.setMaximum(1000)
        self.Resistencia.setOrientation(QtCore.Qt.Horizontal)
        self.Resistencia.setObjectName("Resistencia")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(110, 280, 141, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.Voltaje = QtWidgets.QSlider(self.centralwidget)
        self.Voltaje.setGeometry(QtCore.QRect(70, 310, 160, 22))
        self.Voltaje.setMaximum(10)
        self.Voltaje.setOrientation(QtCore.Qt.Horizontal)
        self.Voltaje.setObjectName("Voltaje")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(110, 360, 141, 21))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.Capacitancia = QtWidgets.QSlider(self.centralwidget)
        self.Capacitancia.setGeometry(QtCore.QRect(70, 390, 160, 22))
        self.Capacitancia.setMaximum(100)
        self.Capacitancia.setOrientation(QtCore.Qt.Horizontal)
        self.Capacitancia.setObjectName("Capacitancia")
        self.Res = QtWidgets.QLabel(self.centralwidget)
        self.Res.setGeometry(QtCore.QRect(240, 240, 111, 21))
        self.Res.setAlignment(QtCore.Qt.AlignCenter)
        self.Res.setObjectName("Res")
        self.Vol = QtWidgets.QLabel(self.centralwidget)
        self.Vol.setGeometry(QtCore.QRect(240, 310, 111, 21))
        self.Vol.setAlignment(QtCore.Qt.AlignCenter)
        self.Vol.setObjectName("Vol")
        self.Cap = QtWidgets.QLabel(self.centralwidget)
        self.Cap.setGeometry(QtCore.QRect(240, 390, 111, 21))
        self.Cap.setAlignment(QtCore.Qt.AlignCenter)
        self.Cap.setObjectName("Cap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Resistencia.valueChanged.connect(self.datos)
        self.Capacitancia.valueChanged.connect(self.datos)
        self.Voltaje.valueChanged.connect(self.datos)

        self.configurar()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Laura V Valiente</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Carga y Descarga Condensador</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">David A Rodriguez</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nicolas D Villamil</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Camilo Piracoca</span></p><p><br/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">2024</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">EP1. Algoritmos Robotica</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Resistencia</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Grafica</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Voltaje</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Capacitancia</span></p></body></html>"))
        self.Res.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Vol.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Cap.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
    
    def configurar(self):

        self.figure = Figure(figsize=(2.5, 1.5))
        self.canvas = FigureCanvas(self.figure)
        self.scene.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Tiempo (s)")
        self.ax.set_ylabel("Voltaje (V)")
        self.datos() 

    def datos(self):

        self.Res.setText(f"{self.Resistencia.value()} Ohm")  
        self.Vol.setText(f"{self.Voltaje.value()} Volts")  
        self.Cap.setText(f"{self.Capacitancia.value()} mF") 
        R = self.Resistencia.value()  
        C = self.Capacitancia.value() / 10000
        V = self.Voltaje.value() 

        t = np.linspace(0, 1, 4000)

        Carga = self.carga(V, R, C, t)
        Descarga = self.descarga(V, R, C, t)

        self.ax.clear()
        self.ax.plot(t, Carga, label="Carga")
        self.ax.plot(t, Descarga, label="Descarga", linestyle="--")
        self.ax.set_xlabel("Tiempo (s)")
        self.ax.set_ylabel("Voltaje (V)")
        self.ax.legend()
        self.canvas.draw()

    def carga(self, V, R, C, t):
        return V * (1 - np.exp(-t / (R * C)))

    def descarga(self, V, R, C, t):
        return V * np.exp(-t / (R * C))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
