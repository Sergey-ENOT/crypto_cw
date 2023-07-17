import os
import sys
from PyQt5 import QtWidgets, QtGui
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
        CryptoWindow.setWindowIcon(self, QtGui.QIcon("fstek.png"))
        self.ui.label_current_text_status.setText("Зашифрование")
        self.ui.checkBox_autofill.setChecked(True)

    def connect_signals(self):
        self.ui.pushButton_change_file_mode.clicked.connect(self.change_operation)
        self.ui.pushButton_change_text_mode.clicked.connect(self.change_operation)
        self.ui.pushButton_execute_text_mode.clicked.connect(self.execute_text)
        self.ui.pushButton_execute_file_mode.clicked.connect(self.execute_file)
        self.ui.pushButton_open_file.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_save_file.clicked.connect(self.save_file_dialog)

    def change_paths(self):
        path_open = self.ui.lineEdit_open_path.text()
        path_save = self.ui.lineEdit_save_path.text()
        self.ui.lineEdit_open_path.setText(path_save)
        self.ui.lineEdit_save_path.setText(path_open)

    def auto_path_save(self, operation):
        if operation == "Зашифрование":
            temp_path = self.path_open + ".kasumi"
            self.path_save = temp_path
            self.ui.lineEdit_save_path.setText(str(temp_path))
        else:
            temp_path = os.path.splitext(self.path_open)[0]
            self.path_save = temp_path
            self.ui.lineEdit_save_path.setText(str(temp_path))

    def open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Выберите файл для открытия", "",
                                              "All Files (*);;Text Files (*.txt)")
        if file:
            self.path_open = file
            self.ui.lineEdit_open_path.setText(str(self.path_open))
            if self.ui.checkBox_autofill.isChecked():
                self.auto_path_save(self.ui.label_current_file_status.text())

    def save_file_dialog(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Выберите файл для сохранения", "",
                                                   "Text Files (*.txt);;All Files (*)")
        if file_name:
            self.path_save = file_name
            self.ui.lineEdit_save_path.setText(str(self.path_save))

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
        if self.ui.checkBox_change_paths.isChecked():
            self.change_paths()

    def use_chiper(self, in_text, input_mode, mode_cbc=False):
        self.kasumi.set_key(self.ui.lineEdit_user_key.text().encode("utf-8").hex())
        if input_mode == "text":
            if self.encryption_status:
                try:
                    return self.kasumi.encrypt(in_text.encode("utf-8").hex(), mode_cbc)
                except Exception as err:
                    self.show_messagebox("critical", "Critical", str(err))
                    return None
            else:
                hex_res = ""
                try:
                    hex_res = self.kasumi.decrypt(in_text, mode_cbc)
                    bytes_res_dec = bytes.fromhex(hex_res[2:])
                    res_utf_8 = bytes_res_dec.decode("utf-8")
                    return res_utf_8
                except UnicodeDecodeError:
                    return hex_res[2:]
                except ValueError:
                    self.show_messagebox("critical", "Critical", "Ошибка расшифрования. Неверный вход")
                    return None
        if input_mode == "file":
            if self.encryption_status:
                try:
                    return self.kasumi.encrypt_file(self.ui.lineEdit_open_path.text(),
                                                    self.ui.lineEdit_save_path.text(),
                                                    mode_cbc)
                except Exception as err:
                    self.show_messagebox("critical", "Critical", str(err))
                    return None
            else:
                try:
                    res_dec_file = self.kasumi.decrypt_file(self.ui.lineEdit_open_path.text(),
                                                            self.ui.lineEdit_save_path.text(),
                                                            mode_cbc)
                    return res_dec_file
                except ValueError:
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
            if self.ui.radioButton_cbc_tm.isChecked():
                mode_enc = True
            res_operation = self.use_chiper(self.ui.plainTextEdit_input.toPlainText(), "text", mode_enc)
            self.ui.plainTextEdit_output.setPlainText(str(res_operation))

    def execute_file(self):
        text_inf = "Пустое значение"
        if self.check_empty(self.ui.lineEdit_open_path.text()):
            self.show_messagebox("warning", "Warning", text_inf + " пути открытия файла")
        elif self.check_empty(self.ui.lineEdit_save_path.text()):
            self.show_messagebox("warning", "Warning", text_inf + " пути сохранения файла")
        elif self.check_empty(self.ui.lineEdit_user_key.text()):
            self.show_messagebox("warning", "Warning", text_inf + " ключа")
        else:
            mode_enc = False
            if self.ui.radioButton_cbc_fm.isChecked():
                mode_enc = True
            self.ui.label_status_operation_text.setText("выполнение операции начато")
            self.ui.label_status_operation_text.repaint()
            res_operation = self.use_chiper(in_text="", input_mode="file", mode_cbc=mode_enc)
            if res_operation is not None:
                self.ui.label_status_operation_text.setText("выполнение операции завершено")
                self.ui.label_status_operation_text.repaint()
                self.show_messagebox("information", "Information about operation", str(res_operation))
            self.ui.label_status_operation_text.setText("")


app = QtWidgets.QApplication([])
main_w = CryptoWindow()
main_w.show()
sys.exit(app.exec())
