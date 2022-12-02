from asterisk.ami import AMIClient
from asterisk.ami import SimpleAction
from  PySide2 import QtWidgets , QtCore
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from Custom_Widgets.Widgets import *
from vista.ui_integrantes import Ui_integrantes
class integrantes(QtWidgets.QMainWindow):#Boton es cambiable
    
    def __init__(self, parent=None):        
        super(integrantes, self).__init__(parent)#Boton es cambiable
        self.ventintegrantes = Ui_integrantes()# Particula
        self.ventintegrantes.setupUi(self)
        self.ventintegrantes.btn_cerrar.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()
         
    
