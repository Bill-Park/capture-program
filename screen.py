import sys
from PyQt5.QtWidgets import QApplication
import test_ui
import os
import bill
import save_gdrive
import json

def pb_test() :
    print("pb test")

def copytoclipboard(text) :
    command_copy = 'echo ' + text.strip() + ' | clip'
    os.system(command_copy)

if __name__ == '__main__' :

    app = QApplication(sys.argv)
    gui = test_ui.Ui_Image_Viewer_2()
    gui.MainWindow.show()


    with open('owner_data.json') as json_file :
        data = json.load(json_file)

    if 'folder_name' in data :
        folder_id_dict = {'folder_id' : save_gdrive.name2id(data['folder_name'])}

    else :
        folder_id_dict = {'folder_id': data['base_dir_id']}

    data.update(folder_id_dict)

    with open('owner_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    gui.select_image(bill.cap_dir)

    sys.exit(app.exec_())

