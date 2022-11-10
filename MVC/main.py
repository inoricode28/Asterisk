########################################################################
# IMPORT CUSTOM BUTTONS FILE
# Because ill be frequently updating this package,
# run "pip install --upgrade QT-PyQt-PySide-Custom-Widgets"
# to install any updates
from Custom_Widgets.Widgets import *

from PySide2.QtCore import *
########################################################################
#QCustomQPushButton esto se pone en la particula
# aqui se ejecuta todo el programa
import sys
# ------ Importacion PySide2 ------
#from PySide2 import QtWidgets
#from PySide2 import QtCore
from controlador.botones import Clark #tambien se modificable
#Una modificacion
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_ses = Clark()#Clark es modificable
    #ventana_ses = Tranferencia()
    ventana_ses.show()
    sys.exit(app.exec_())