import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
#from PyQt5.QtGui import
import test_ui
import os
import bill

cap_dir = os.path.join('f:\\', 'blogging', 'capture')
dir_id = bill.dir_id

def pb_test() :
    print("pb test")

def copytoclipboard(text) :
    command_copy = 'echo ' + text.strip() + ' | clip'
    os.system(command_copy)

if __name__ == '__main__' :

    app = QApplication(sys.argv)
    gui = test_ui.Ui_Image_Viewer_2()
    gui.MainWindow.show()

    image_list = os.listdir(cap_dir)
    pick_image = ""

    if len(image_list) > 1 :
        pick_image = gui.browse_folder()

    else :
        pick_image = os.path.join(cap_dir, image_list[0])

    gui.upload_image(pick_image)
    command_str = 'gdrive upload ' + pick_image + ' --share -p ' + dir_id
    print(command_str)
    system_echo = os.popen(command_str).read()
    image_id = str(system_echo.split()[3])
    base_url = 'https://drive.google.com/uc?id=' + image_id.strip()
    shorten_url = bill.short_url(base_url)
    print(shorten_url)
    copytoclipboard(shorten_url)
    gui.address_box.setText(shorten_url)

    #gui.label.setText(base_url)
    #https://goo.gl/3jvME3
    #os.remove(pick_image)

    sys.exit(app.exec_())


'''
app = QApplication(sys.argv)
form = test_design.Ui_Form()
form.show()
app.exec_()
'''
'''
w = QWidget()
w.resize(250,150)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())
'''
