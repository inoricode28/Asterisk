from  PySide2 import QtWidgets , QtCore
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from Custom_Widgets.Widgets import *
#Vista.ui_botones eso signidica Carpeta.archivo
#from vista.ui_botones import Ui_MainWindow #Ui_MainWindow es la clase que se encuentra en la particula
from vista.ui_botones import Ui_MainWindow
#El nombre de la clase es cambiable
#Driver el controlador
class Clark(QtWidgets.QMainWindow):#Boton es cambiable
    
    def __init__(self, *args , parent=None):
        
        super(Clark, self).__init__(parent)#Boton es cambiable
        self.ventPrin = Ui_MainWindow()# Particula
        self.ventPrin.setupUi(self)         
        #self.ventPrin.pushButton_5.clicked.connect(lambda: self.close())
        #self.ventPrin.pushButton_6.clicked.connect(self.cerrar)
        loadJsonStyle(self, self.ventPrin)

        self.ventPrin.pushButton.setObjectTheme(1)
        self.ventPrin.pushButton_2.setObjectTheme(2)
        self.ventPrin.pushButton_3.setObjectTheme(3)
        self.ventPrin.pushButton_4.setObjectTheme(4)
        self.ventPrin.pushButton_5.setObjectTheme(5)
        self.ventPrin.pushButton_6.setObjectTheme(6)
        self.ventPrin.pushButton_7.setObjectTheme(11)
        self.ventPrin.pushButton_5.setObjectTheme(10)
        self.ventPrin.pushButton_8.setObjectTheme(12)
        self.ventPrin.pushButton_9.setObjectTheme(13)
        self.ventPrin.pushButton.setObjectCustomTheme("#fff", "#000")
        self.ventPrin.pushButton.setObjectAnimateOn("hover")
        self.ventPrin.pushButton_7.setObjectAnimateOn("click")
        #self.ventPrin.pushButton._animation.setEasingCurve(QtCore.QEasingCurve.InOutElastic)
        self.ventPrin.pushButton._animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
    
    #def cerrar(self):
        #self.close()
        
    