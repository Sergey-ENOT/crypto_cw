# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\course_work\ui_files\crypto_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 0, 790, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")
        self.pushButton_execute_file_mode = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_execute_file_mode.setGeometry(QtCore.QRect(650, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_execute_file_mode.setFont(font)
        self.pushButton_execute_file_mode.setObjectName("pushButton_execute_file_mode")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_file)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_current_file_mode = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_current_file_mode.setFont(font)
        self.label_current_file_mode.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_current_file_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_file_mode.setObjectName("label_current_file_mode")
        self.verticalLayout_6.addWidget(self.label_current_file_mode)
        self.label_current_file_status = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_current_file_status.setFont(font)
        self.label_current_file_status.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_current_file_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_file_status.setObjectName("label_current_file_status")
        self.verticalLayout_6.addWidget(self.label_current_file_status)
        self.pushButton_change_file_mode = QtWidgets.QPushButton(self.tab_file)
        self.pushButton_change_file_mode.setGeometry(QtCore.QRect(170, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_change_file_mode.setFont(font)
        self.pushButton_change_file_mode.setObjectName("pushButton_change_file_mode")
        self.layoutWidget = QtWidgets.QWidget(self.tab_file)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 90, 651, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_open_path = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_open_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_open_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_open_path.setFont(font)
        self.lineEdit_open_path.setObjectName("lineEdit_open_path")
        self.verticalLayout_4.addWidget(self.lineEdit_open_path)
        self.lineEdit_save_path = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_save_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_save_path.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_save_path.setFont(font)
        self.lineEdit_save_path.setObjectName("lineEdit_save_path")
        self.verticalLayout_4.addWidget(self.lineEdit_save_path)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_file)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 103, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_open_file = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(92)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open_file.sizePolicy().hasHeightForWidth())
        self.pushButton_open_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_open_file.setFont(font)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.verticalLayout_5.addWidget(self.pushButton_open_file)
        self.pushButton_save_file = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_file.sizePolicy().hasHeightForWidth())
        self.pushButton_save_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save_file.setFont(font)
        self.pushButton_save_file.setObjectName("pushButton_save_file")
        self.verticalLayout_5.addWidget(self.pushButton_save_file)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_file)
        self.layoutWidget_3.setGeometry(QtCore.QRect(390, 10, 151, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_mode_encryption_fm = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_mode_encryption_fm.setFont(font)
        self.label_mode_encryption_fm.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_mode_encryption_fm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mode_encryption_fm.setObjectName("label_mode_encryption_fm")
        self.verticalLayout_8.addWidget(self.label_mode_encryption_fm)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_cbc_fm = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_cbc_fm.setChecked(True)
        self.radioButton_cbc_fm.setObjectName("radioButton_cbc_fm")
        self.horizontalLayout_3.addWidget(self.radioButton_cbc_fm)
        self.radioButton_ecb_fm = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_ecb_fm.setObjectName("radioButton_ecb_fm")
        self.horizontalLayout_3.addWidget(self.radioButton_ecb_fm)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.checkBox_autofill = QtWidgets.QCheckBox(self.tab_file)
        self.checkBox_autofill.setGeometry(QtCore.QRect(10, 190, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_autofill.setFont(font)
        self.checkBox_autofill.setObjectName("checkBox_autofill")
        self.checkBox_change_paths = QtWidgets.QCheckBox(self.tab_file)
        self.checkBox_change_paths.setGeometry(QtCore.QRect(10, 220, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_change_paths.setFont(font)
        self.checkBox_change_paths.setObjectName("checkBox_change_paths")
        self.widget = QtWidgets.QWidget(self.tab_file)
        self.widget.setGeometry(QtCore.QRect(10, 350, 761, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_status_operation = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_status_operation.setFont(font)
        self.label_status_operation.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid red;")
        self.label_status_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_operation.setObjectName("label_status_operation")
        self.verticalLayout_9.addWidget(self.label_status_operation)
        self.label_status_operation_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_status_operation_text.setFont(font)
        self.label_status_operation_text.setStyleSheet("border-radius: 6px;\n"
"border: 2px solid red;")
        self.label_status_operation_text.setText("")
        self.label_status_operation_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_operation_text.setObjectName("label_status_operation_text")
        self.verticalLayout_9.addWidget(self.label_status_operation_text)
        self.tabWidget.addTab(self.tab_file, "")
        self.tab_text = QtWidgets.QWidget()
        self.tab_text.setObjectName("tab_text")
        self.label_output_text = QtWidgets.QLabel(self.tab_text)
        self.label_output_text.setGeometry(QtCore.QRect(430, 350, 101, 16))
        self.label_output_text.setText("")
        self.label_output_text.setObjectName("label_output_text")
        self.pushButton_change_text_mode = QtWidgets.QPushButton(self.tab_text)
        self.pushButton_change_text_mode.setGeometry(QtCore.QRect(170, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_change_text_mode.setFont(font)
        self.pushButton_change_text_mode.setObjectName("pushButton_change_text_mode")
        self.pushButton_execute_text_mode = QtWidgets.QPushButton(self.tab_text)
        self.pushButton_execute_text_mode.setGeometry(QtCore.QRect(650, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_execute_text_mode.setFont(font)
        self.pushButton_execute_text_mode.setObjectName("pushButton_execute_text_mode")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_text)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 100, 761, 321))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_input = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_input.setFont(font)
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        self.verticalLayout.addWidget(self.plainTextEdit_input)
        self.label_input_text = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_input_text.setFont(font)
        self.label_input_text.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_input_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_text.setObjectName("label_input_text")
        self.verticalLayout.addWidget(self.label_input_text)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_output.setFont(font)
        self.plainTextEdit_output.setAutoFillBackground(False)
        self.plainTextEdit_output.setTabChangesFocus(False)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setPlainText("")
        self.plainTextEdit_output.setOverwriteMode(False)
        self.plainTextEdit_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.verticalLayout_2.addWidget(self.plainTextEdit_output)
        self.label_output_text_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_output_text_2.setFont(font)
        self.label_output_text_2.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_output_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_text_2.setObjectName("label_output_text_2")
        self.verticalLayout_2.addWidget(self.label_output_text_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_text)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_current_text_mode = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_current_text_mode.setFont(font)
        self.label_current_text_mode.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_current_text_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_text_mode.setObjectName("label_current_text_mode")
        self.verticalLayout_3.addWidget(self.label_current_text_mode)
        self.label_current_text_status = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_current_text_status.setFont(font)
        self.label_current_text_status.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_current_text_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_text_status.setObjectName("label_current_text_status")
        self.verticalLayout_3.addWidget(self.label_current_text_status)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_text)
        self.layoutWidget4.setGeometry(QtCore.QRect(390, 10, 151, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_mode_encryption_tm = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_mode_encryption_tm.setFont(font)
        self.label_mode_encryption_tm.setStyleSheet("border: 1px  solid rgb(255, 0, 0);")
        self.label_mode_encryption_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mode_encryption_tm.setObjectName("label_mode_encryption_tm")
        self.verticalLayout_7.addWidget(self.label_mode_encryption_tm)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_cbc_tm = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_cbc_tm.setChecked(True)
        self.radioButton_cbc_tm.setObjectName("radioButton_cbc_tm")
        self.horizontalLayout.addWidget(self.radioButton_cbc_tm)
        self.radioButton_ecb_tm = QtWidgets.QRadioButton(self.layoutWidget4)
        self.radioButton_ecb_tm.setObjectName("radioButton_ecb_tm")
        self.horizontalLayout.addWidget(self.radioButton_ecb_tm)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_text, "")
        self.lineEdit_user_key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user_key.setGeometry(QtCore.QRect(80, 470, 701, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user_key.setFont(font)
        self.lineEdit_user_key.setObjectName("lineEdit_user_key")
        self.label_user_key = QtWidgets.QLabel(self.centralwidget)
        self.label_user_key.setGeometry(QtCore.QRect(8, 470, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_user_key.setFont(font)
        self.label_user_key.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_user_key.setObjectName("label_user_key")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptographyApp"))
        self.pushButton_execute_file_mode.setText(_translate("MainWindow", "Выполнить"))
        self.label_current_file_mode.setText(_translate("MainWindow", "Текущая операция:"))
        self.label_current_file_status.setText(_translate("MainWindow", "Зашифрование"))
        self.pushButton_change_file_mode.setText(_translate("MainWindow", "сменить операцию"))
        self.pushButton_open_file.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_save_file.setText(_translate("MainWindow", "Сохранить файл"))
        self.label_mode_encryption_fm.setText(_translate("MainWindow", "Режим шифрования"))
        self.radioButton_cbc_fm.setText(_translate("MainWindow", "CBC"))
        self.radioButton_ecb_fm.setText(_translate("MainWindow", "ECB"))
        self.checkBox_autofill.setText(_translate("MainWindow", "Автозаполнение пути сохранения файла"))
        self.checkBox_change_paths.setText(_translate("MainWindow", "Менять местами пути открытия и сохранения файла при смене операции"))
        self.label_status_operation.setText(_translate("MainWindow", "информация о выполнении операции"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "File Mode"))
        self.pushButton_change_text_mode.setText(_translate("MainWindow", "сменить операцию"))
        self.pushButton_execute_text_mode.setText(_translate("MainWindow", "Выполнить"))
        self.label_input_text.setText(_translate("MainWindow", "Входной текст"))
        self.label_output_text_2.setText(_translate("MainWindow", "Выходной текст"))
        self.label_current_text_mode.setText(_translate("MainWindow", "Текущая операция:"))
        self.label_current_text_status.setText(_translate("MainWindow", "Шифрование"))
        self.label_mode_encryption_tm.setText(_translate("MainWindow", "Режим шифрования"))
        self.radioButton_cbc_tm.setText(_translate("MainWindow", "CBC"))
        self.radioButton_ecb_tm.setText(_translate("MainWindow", "ECB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_text), _translate("MainWindow", "Text Mode"))
        self.label_user_key.setText(_translate("MainWindow", "Ключ:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
