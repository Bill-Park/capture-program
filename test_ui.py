# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import bill
import quickstart
import httplib2
import save_gdrive
from apiclient import discovery

def copytoclipboard(text) :
    command_copy = 'echo ' + text.strip() + ' | clip'
    os.system(command_copy)

class Ui_Image_Viewer_2(QtWidgets.QMainWindow):
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

    def browse_folder(self) :
        #directory = QtWidgets.QFileDialog.getExistingDirectory(self, "pick folder")
        path_dialog = QtWidgets.QFileDialog()
        QtWidgets.QFileDialog.setDirectory(path_dialog, os.path.join('f:\\', 'blogging', 'capture'))
        image_path, _ = path_dialog.getOpenFileName(self, "pick image")
        self.upload_image(image_path)
        return image_path

    def get_url(self, image_path) :
        if image_path is not None:
            command_str = 'gdrive upload ' + image_path + ' --share -p ' + bill.dir_id
            print(command_str)
            system_echo = os.popen(command_str).read()
            image_id = str(system_echo.split()[3])
            base_url = 'https://drive.google.com/uc?id=' + image_id.strip()
            shorten_url = bill.short_url(base_url)
            #print(shorten_url)
            copytoclipboard(shorten_url)
            self.address_box.setText(shorten_url)

            os.remove(image_path)

    def upload_image(self, image_path) :
        image = QtGui.QImage(image_path)
        pixmap_raw = QtGui.QPixmap.fromImage(image)
        height_scale = self.Image_Viewer.height() / pixmap_raw.height() * 1.0
        width_scale = self.Image_Viewer.width() / pixmap_raw.width() * 1.0

        view_scale = height_scale if height_scale < width_scale else width_scale
        '''
        if height_scale < width_scale :
            view_scale = height_scale
        else :
            view_scale = width_scale
        '''
        print("uploading")
        pixmap_resize = pixmap_raw.scaled(round(pixmap_raw.width() * view_scale), round(pixmap_raw.height() * view_scale))
        self.Image_Viewer.setPixmap(pixmap_resize)
        print("upload end")

    def select_image(self, image_dir) :
        pick_image = ""
        image_list = os.listdir(image_dir)
        if len(image_list) > 1 :
            pick_image = self.browse_folder()
        elif len(image_list) == 1 :
            pick_image = os.path.join(bill.cap_dir, image_list[0])
        else :
            self.Image_Viewer.setText(" No Image")
            return None

        #self.upload_image(pick_image)
        self.get_url(pick_image)
        return pick_image

    def drive_api(self) :
        credentials = quickstart.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)
        result = service.files().list(pageSize=50).execute()
        items = result.get('files', [])
        print(items)

    def __init__(self) :
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.pick_button.clicked.connect(self.browse_folder)
        self.reload_button.clicked.connect(lambda: self.select_image(bill.cap_dir))
        #lambda make select_image's return nothing