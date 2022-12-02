# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'integrantesPdXTfD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets.Widgets import *


class Ui_integrantes(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 30, 401, 91))
        font = QFont()
        font.setFamily(u"Berlin Sans FB")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(176, 37, 200);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 140, 631, 331))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(28)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(200, 53, 198);")
        self.btn_cerrar = QPushButton(self.centralwidget)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        self.btn_cerrar.setGeometry(QRect(150, 490, 531, 81))
        self.btn_cerrar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"LogotipoUCV_Versi\u00f3nLarga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon)
        self.btn_cerrar.setIconSize(QSize(512, 512))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Integrates", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ovalle P\u00e9rez, Helleny Solanch\n"
"Policarpo Mu\u00f1oz, Katherin Shirley \n"
"Quispe Flores, Arturo David Mirko \n"
"Rodriguez Romero, Leonardo Jeremy \n"
"Rojas Aivar, John Jonathan \n"
"Tello Moreno, Eduardo Paoly", None))
        self.btn_cerrar.setText("")
    # retranslateUi

