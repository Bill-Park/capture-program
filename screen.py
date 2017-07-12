import sys
from PyQt5.QtWidgets import QApplication
import test_ui
import os
import bill
import save_gdrive

def pb_test() :
    print("pb test")

def copytoclipboard(text) :
    command_copy = 'echo ' + text.strip() + ' | clip'
    os.system(command_copy)

if __name__ == '__main__' :

    app = QApplication(sys.argv)
    gui = test_ui.Ui_Image_Viewer_2()
    gui.MainWindow.show()

    if os.path.exists(bill.parents_folder) :
        f = open(bill.parents_folder, 'r')
        parents_folder_name = f.readline()
        f.close()
        bill.dir_id = save_gdrive.name2id(parents_folder_name)
        print(bill.dir_id)

    pick_image = gui.select_image(bill.cap_dir)

    sys.exit(app.exec_())

