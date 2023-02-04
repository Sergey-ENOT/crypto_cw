import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from py_files.crypto_UI import Ui_MainWindow


class CryptoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CryptoWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.encryption_status = True
        self.update_ui()
        self.connect_signals()
        self.path_open = ""
        self.path_save = ""
        self.messagebox = QMessageBox()

    def update_ui(self):
        self.ui.plainTextEdit_output.setPlainText("Russia")

    def connect_signals(self):
        self.ui.pushButton_change_file_mode.clicked.connect(self.change_mode)
        self.ui.pushButton_change_text_mode.clicked.connect(self.change_mode)
        self.ui.pushButton_execute_text_mode.clicked.connect(self.execute_text)
        self.ui.pushButton_open_file.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_save_file.clicked.connect(self.save_file_dialog)

    def clear_path_save(self):
        temp_path = os.path.splitext(self.path_open)[0]
        temp_path += ".txt"
        self.ui.label_path_save.setText(str(temp_path))

    def open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()", "",
                                              "All Files (*);;Text Files (*.txt)")
        if file:
            self.path_open = file
            self.ui.label_path_open.setText(str(self.path_open))
            if self.ui.checkBox_auto_fill.isChecked():
                self.clear_path_save()

    def save_file_dialog(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.path_save = file_name
            self.ui.label_path_save.setText(str(self.path_save))

    def show_messagebox(self, level, title, text):
        if level == "critical":
            self.messagebox.setIcon(QMessageBox.Critical)
        elif level == "warning":
            self.messagebox.setIcon(QMessageBox.Warning)
        elif level == "information":
            self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.setWindowTitle(title)
        self.messagebox.setText(text)
        self.messagebox.exec()

    def change_mode(self):
        if self.encryption_status:
            self.ui.label_current_file_status.setText("Дешифрование")
            self.ui.label_current_text_status.setText("Дешифрование")
            self.encryption_status = False
        else:
            self.ui.label_current_file_status.setText("Шифрование")
            self.ui.label_current_text_status.setText("Шифрование")
            self.encryption_status = True

    def execute_text(self):
        writen_text = self.ui.plainTextEdit_input.toPlainText()
        self.ui.plainTextEdit_output.setPlainText(writen_text)


app = QtWidgets.QApplication([])
main_w = CryptoWindow()
main_w.show()
sys.exit(app.exec())
