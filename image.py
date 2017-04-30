# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Image_Viewer_2(object):
    def setupUi(self, Image_Viewer_2):
        Image_Viewer_2.setObjectName("Image_Viewer_2")
        Image_Viewer_2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Image_Viewer_2)
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
        self.address_box.setGeometry(QtCore.QRect(90, 470, 320, 25))
        self.address_box.setDragEnabled(True)
        self.address_box.setReadOnly(True)
        self.address_box.setObjectName("address_box")
        self.reload_button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_button.setGeometry(QtCore.QRect(415, 470, 50, 25))
        self.reload_button.setObjectName("reload_button")
        Image_Viewer_2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Image_Viewer_2)
        self.statusbar.setObjectName("statusbar")
        Image_Viewer_2.setStatusBar(self.statusbar)

        self.retranslateUi(Image_Viewer_2)
        QtCore.QMetaObject.connectSlotsByName(Image_Viewer_2)

    def retranslateUi(self, Image_Viewer_2):
        _translate = QtCore.QCoreApplication.translate
        Image_Viewer_2.setWindowTitle(_translate("Image_Viewer_2", "MainWindow"))
        self.pick_button.setText(_translate("Image_Viewer_2", "pick_image"))
        self.reload_button.setText(_translate("Image_Viewer_2", "reload"))

