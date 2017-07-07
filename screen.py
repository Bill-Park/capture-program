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
