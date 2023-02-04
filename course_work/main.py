import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from py_files.crypto_UI import Ui_MainWindow


class CryptoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CryptoWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
main_w = CryptoWindow()
main_w.show()
sys.exit(app.exec())
