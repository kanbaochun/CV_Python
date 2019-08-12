# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cvWindow(object):
    def setupUi(self, cvWindow):
        cvWindow.setObjectName("cvWindow")
        cvWindow.resize(1200, 1100)
        
        self.centralwidget = QtWidgets.QWidget(cvWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.display = QtWidgets.QGraphicsView(self.centralwidget)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)

        self.camera = QtWidgets.QCheckBox(self.centralwidget)
        self.camera.setObjectName("camera")
        self.verticalLayout.addWidget(self.camera)

        self.localFile = QtWidgets.QCheckBox(self.centralwidget)
        self.localFile.setObjectName("localFile")
        self.verticalLayout.addWidget(self.localFile)

        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setObjectName("Open")
        self.verticalLayout.addWidget(self.Open)

        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setObjectName("Close")
        self.verticalLayout.addWidget(self.Close)
        
        cvWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cvWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        cvWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cvWindow)
        self.statusbar.setObjectName("statusbar")
        cvWindow.setStatusBar(self.statusbar)

        self.retranslateUi(cvWindow)
        QtCore.QMetaObject.connectSlotsByName(cvWindow)

    def retranslateUi(self, cvWindow):
        _translate = QtCore.QCoreApplication.translate
        cvWindow.setWindowTitle(_translate("cvWindow", "MainWindow"))
        
        self.camera.setText(_translate("cvWindow", "Camera"))
        self.localFile.setText(_translate("cvWindow", "Localfile"))
        self.Open.setText(_translate("cvWindow", "Open"))
        self.Close.setText(_translate("cvWindow", "Close"))

