from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
        
        self.Seleccionar = QtWidgets.QPushButton(self.centralwidget)
        self.Seleccionar.setGeometry(QtCore.QRect(360, 200, 81, 21))
        self.Seleccionar.setObjectName("Seleccionar")
        
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
        self.label_15.setGeometry(QtCore.QRect(260, 480, 151, 31))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        
        # Cambiar a QLabel para mostrar imágenes
        self.Grafica = QLabel(self.centralwidget)
        self.Grafica.setGeometry(QtCore.QRect(70, 270, 256, 192))
        self.Grafica.setObjectName("Grafica")
        
        self.Grafica_2 = QLabel(self.centralwidget)
        self.Grafica_2.setGeometry(QtCore.QRect(370, 270, 256, 192))
        self.Grafica_2.setObjectName("Grafica_2")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 200, 141, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 240, 141, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 240, 141, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        
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
        self.Seleccionar.clicked.connect(self.cargar_imagen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Laura V Valiente</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Contornos</span></p></body></html>"))
        self.Seleccionar.setText(_translate("MainWindow", "Seleccionar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">David A Rodriguez</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nicolas D Villamil</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Camilo Piracoca</span></p><p><br/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">2024</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">EP Algoritmos Robotica</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Abrir Imagen:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Original</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contorno</span></p></body></html>"))

    def cargar_imagen(self):
        # Abrir un cuadro de diálogo para seleccionar la imagen
        file_path, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Selecciona una imagen', '', 
                                                    'Image files (*.jpg *.jpeg *.png *.gif)')
        if file_path:
            # Cargar y mostrar la imagen
            pixmap = QPixmap(file_path)
            self.Grafica.setPixmap(pixmap.scaled(256, 192, QtCore.Qt.KeepAspectRatio))  # Ajustar tamaño
            self.obtener_contornos(file_path)

    def reducir_resolucion(self,img, escala):
        ancho = int(img.shape[1] * escala)
        alto = int(img.shape[0] * escala)
        return cv2.resize(img, (ancho, alto), interpolation=cv2.INTER_AREA)

    def obtener_contornos(self,image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = self.reducir_resolucion(img, 0.4) 
        _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        contornos, _ = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        self.dibujar_contornos(img, contornos)

    def dibujar_contornos(self, img, contornos):
        # Crear una imagen en blanco para dibujar los contornos
        img_contornos = np.zeros_like(img)
        for contorno in contornos:
            cv2.drawContours(img_contornos, [contorno], -1, (255, 255, 255), 1)

        # Convertir la imagen a formato adecuado para QLabel
        height, width = img_contornos.shape
        bytes_per_line = width
        q_img = QtGui.QImage(img_contornos.data, width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)

        # Mostrar la imagen de contornos en Grafica_2
        self.Grafica_2.setPixmap(QPixmap.fromImage(q_img).scaled(256, 192, QtCore.Qt.KeepAspectRatio))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())