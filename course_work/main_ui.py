import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from py_files.crypto_UI import Ui_MainWindow
from kasumi import Kasumi


class CryptoWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CryptoWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.encryption_status = True
        self.mode_enc_status = True
        self.update_ui()
        self.connect_signals()
        self.path_open = ""
        self.path_save = ""
        self.messagebox = QMessageBox()
        self.kasumi = Kasumi()

    def update_ui(self):
        self.ui.label_current_text_status.setText("Зашифрование")

    def connect_signals(self):
        self.ui.pushButton_change_file_mode.clicked.connect(self.change_operation)
        self.ui.pushButton_change_text_mode.clicked.connect(self.change_operation)
        self.ui.pushButton_execute_text_mode.clicked.connect(self.execute_text)
        self.ui.pushButton_open_file.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_save_file.clicked.connect(self.save_file_dialog)

    def auto_path_save(self):
        temp_path = os.path.splitext(self.path_open)[0]
        temp_path += ".txt"
        self.path_save = temp_path
        self.ui.label_path_save.setText(str(temp_path))

    def open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для открытия", "",
                                              "All Files (*);;Text Files (*.txt)")
        if file:
            self.path_open = file
            self.ui.label_path_open.setText(str(self.path_open))

    def save_file_dialog(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Выберите файл для сохранения", "",
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

    @staticmethod
    def check_empty(text_value):
        if text_value.strip() == "":
            return True
        return False

    def change_operation(self):
        if self.encryption_status:
            self.ui.label_current_file_status.setText("Расшифрование")
            self.ui.label_current_text_status.setText("Расшифрование")
            self.encryption_status = False
        else:
            self.ui.label_current_file_status.setText("Зашифрование")
            self.ui.label_current_text_status.setText("Зашифрование")
            self.encryption_status = True

    def use_chiper(self, in_text, input_mode="text", mode_enc=False):
        print("start_use")
        if input_mode == "text":
            print("start_text")
            self.kasumi.set_key(self.ui.lineEdit_user_key.text().encode("utf-8").hex())
            if self.encryption_status:
                try:
                    print("in_text_text:", in_text.encode("utf-8").hex())
                    return self.kasumi.encrypt(in_text.encode("utf-8").hex(), mode_enc)
                except Exception as err:
                    self.show_messagebox("critical", "Critical", str(err))
            else:
                bytes_res_dec = ""
                try:
                    hex_res = self.kasumi.decrypt(in_text, mode_enc)
                    bytes_res_dec = bytes.fromhex(hex_res[2:])
                    print("RES_BYTES:", bytes_res_dec)
                    res_utf_8 = bytes_res_dec.decode("utf-8")
                    return res_utf_8
                except UnicodeDecodeError as err:
                    print("error_UDE:", err)
                    return bytes_res_dec
                except ValueError as err:
                    print("error_VE:", err)
                    self.show_messagebox("critical", "Critical", "Ошибка расшифрования. Неверный вход")
                    return None

    def execute_text(self):
        self.ui.plainTextEdit_output.setPlainText("")
        text_inf = "Пустое значение"
        if self.check_empty(self.ui.plainTextEdit_input.toPlainText()):
            self.show_messagebox("warning", "Warning", text_inf + " входного текста")
        elif self.check_empty(self.ui.lineEdit_user_key.text()):
            self.show_messagebox("warning", "Warning", text_inf + " ключа")
        else:
            mode_enc = False
            if self.ui.radioButton_ecb_tm.isChecked():
                mode_enc = True
            res_operation = self.use_chiper(self.ui.plainTextEdit_input.toPlainText(), "text", mode_enc)
            print("res_op:", res_operation)
            self.ui.plainTextEdit_output.setPlainText(str(res_operation))


app = QtWidgets.QApplication([])
main_w = CryptoWindow()
main_w.show()
sys.exit(app.exec())
