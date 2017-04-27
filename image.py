# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pick_button = QtWidgets.QPushButton(self.centralwidget)
        self.pick_button.setGeometry(QtCore.QRect(5, 470, 75, 25))
        self.pick_button.setObjectName("pick_button")
        self.Image_Viewer = QtWidgets.QLabel(self.centralwidget)
        self.Image_Viewer.setEnabled(True)
        self.Image_Viewer.setGeometry(QtCore.QRect(0, 10, 800, 450))
        self.Image_Viewer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Image_Viewer.setMidLineWidth(0)
        self.Image_Viewer.setText("")
        self.Image_Viewer.setObjectName("Image_Viewer")
        self.address_box = QtWidgets.QLineEdit(self.centralwidget)
        self.address_box.setGeometry(QtCore.QRect(90, 470, 450, 25))
        self.address_box.setDragEnabled(True)
        self.address_box.setReadOnly(True)
        self.address_box.setObjectName("address_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pick_button.setText(_translate("MainWindow", "pick_image"))

