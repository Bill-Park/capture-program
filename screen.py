import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
#from PyQt5.QtGui import
import test_ui

def pb_test() :
    print("pb test")
'''
class MainWindow(QDialog, screen_ui.Ui_MainWindow) :
    def __init__(self, parent=None) :
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
'''

if __name__ == '__main__' :

    app = QApplication(sys.argv)
    m_window = QMainWindow()
    #m_window.setWindowTitle("abc")
    #m_window.show()
    gui = test_ui.Ui_MainWindow(m_window)
    gui.MainWindow.show()
    gui.pushButton.clicked.connect(pb_test)
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
