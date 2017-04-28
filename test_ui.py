# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow) :

    def setupUi(self, MainWindow) :
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

    def browse_folder(self) :
        #directory = QtWidgets.QFileDialog.getExistingDirectory(self, "pick folder")
        image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "pick image")
        #print(image_path)
        self.upload_image(image_path)
        return image_path


    def upload_image(self, image_path) :
        image = QtGui.QImage(image_path)
        pixmap_raw = QtGui.QPixmap.fromImage(image)
        height_scale = self.Image_Viewer.height() / pixmap_raw.height() * 1.0
        width_scale = self.Image_Viewer.width()/ pixmap_raw.width() * 1.0

        view_scale = height_scale if height_scale < width_scale else width_scale
        '''
        if height_scale < width_scale :
            view_scale = height_scale
        else :
            view_scale = width_scale
        '''

        pixmap_resize = pixmap_raw.scaled(round(pixmap_raw.width() * view_scale), round(pixmap_raw.height() * view_scale))
        self.Image_Viewer.setPixmap(pixmap_resize)


    def __init__(self) :
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.pick_button.clicked.connect(self.browse_folder)
