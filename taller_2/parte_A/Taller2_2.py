
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
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
        self.label_7.setGeometry(QtCore.QRect(250, 150, 191, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Seno = QtWidgets.QPushButton(self.centralwidget)
        self.Seno.setGeometry(QtCore.QRect(80, 310, 75, 23))
        self.Seno.setObjectName("Seno")
        self.Coseno = QtWidgets.QPushButton(self.centralwidget)
        self.Coseno.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.Coseno.setObjectName("Coseno")
        self.Tangente = QtWidgets.QPushButton(self.centralwidget)
        self.Tangente.setGeometry(QtCore.QRect(80, 340, 75, 23))
        self.Tangente.setObjectName("Tangente")
        self.Cotangente = QtWidgets.QPushButton(self.centralwidget)
        self.Cotangente.setGeometry(QtCore.QRect(200, 340, 75, 23))
        self.Cotangente.setObjectName("Cotangente")
        self.Cosecante = QtWidgets.QPushButton(self.centralwidget)
        self.Cosecante.setGeometry(QtCore.QRect(200, 310, 75, 23))
        self.Cosecante.setObjectName("Cosecante")
        self.Secante = QtWidgets.QPushButton(self.centralwidget)
        self.Secante.setGeometry(QtCore.QRect(200, 370, 75, 23))
        self.Secante.setObjectName("Secante")
        self.Lim_Inf = QtWidgets.QTextEdit(self.centralwidget)
        self.Lim_Inf.setGeometry(QtCore.QRect(70, 240, 91, 31))
        self.Lim_Inf.setObjectName("Lim_Inf")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 210, 101, 21))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 210, 91, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
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
        self.label_14.setGeometry(QtCore.QRect(290, 480, 81, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(260, 450, 151, 31))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.Lim_sup = QtWidgets.QTextEdit(self.centralwidget)
        self.Lim_sup.setGeometry(QtCore.QRect(200, 240, 91, 31))
        self.Lim_sup.setObjectName("Lim_sup")
        self.Grafica = QtWidgets.QGraphicsView(self.centralwidget)
        self.Grafica.setGeometry(QtCore.QRect(340, 210, 286, 192))
        self.Grafica.setObjectName("Grafica")
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

        self.canvas_layout = QtWidgets.QVBoxLayout(self.Grafica)
        self.figure = Figure(figsize=(0.5, 0.5))
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas_layout.addWidget(self.canvas)
        self.Seno.clicked.connect(self.seno)
        self.Coseno.clicked.connect(self.coseno)
        self.Tangente.clicked.connect(self.tangente)
        self.Cotangente.clicked.connect(self.cotangente)
        self.Cosecante.clicked.connect(self.cosecante)
        self.Secante.clicked.connect(self.secante)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Laura V Valiente</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Trigonometricas</span></p></body></html>"))
        self.Seno.setText(_translate("MainWindow", "Seno"))
        self.Coseno.setText(_translate("MainWindow", "Coseno"))
        self.Tangente.setText(_translate("MainWindow", "Tangente"))
        self.Cotangente.setText(_translate("MainWindow", "Cotangente"))
        self.Cosecante.setText(_translate("MainWindow", "Cosecante"))
        self.Secante.setText(_translate("MainWindow", "Secante"))
        self.Lim_Inf.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Limite Superior:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Limite Inferior:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">David A Rodriguez</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nicolas D Villamil</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Camilo Piracoca</span></p><p><br/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">2024</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">EP Algoritmos Robotica</span></p></body></html>"))
        self.Lim_sup.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    def obtener_limite(self):
        try:
            x_min = float(self.Lim_Inf.toPlainText())
            x_max = float(self.Lim_sup.toPlainText())
        
            if x_min >= x_max:
                raise ValueError("El límite inferior debe ser menor que el límite superior.")
            
        except ValueError:
            x_min, x_max = -20, 20
            QtWidgets.QMessageBox.warning(None, "Error", "Valores inválidos, usando límites predeterminados -20 a 20.")
        
        return np.linspace(x_min, x_max, 1000)
    
    def seno(self):
        x = self.obtener_limite()
        y = np.sin(x)
        self.graficar(x, y)

    def coseno(self):
        x = self.obtener_limite()
        y = np.cos(x)
        self.graficar(x, y)

    def tangente(self):
        x = self.obtener_limite()
        y = np.tan(x)
        self.graficar(x, y)

    def secante(self):
        x = self.obtener_limite()
        y = 1/np.cos(x)
        self.graficar(x, y)

    def cotangente(self):
        x = self.obtener_limite()
        y = 1/np.tan(x)
        self.graficar(x, y)

    def cosecante(self):
        x = self.obtener_limite()
        y = 1/np.sin(x)
        self.graficar(x, y)

    def graficar(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.grid(True)
        self.canvas.draw()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
