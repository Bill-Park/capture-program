import sys
from PyQt5.QtWidgets import QApplication
import test_ui
import os
import bill


cap_dir = bill.cap_dir
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

    pick_image = gui.select_image(bill.cap_dir)
    if pick_image is not None :
        command_str = 'gdrive upload ' + pick_image + ' --share -p ' + dir_id
        print(command_str)
        system_echo = os.popen(command_str).read()
        image_id = str(system_echo.split()[3])
        base_url = 'https://drive.google.com/uc?id=' + image_id.strip()
        shorten_url = bill.short_url(base_url)
        print(shorten_url)
        copytoclipboard(shorten_url)
        gui.address_box.setText(shorten_url)

        os.remove(pick_image)

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
