# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Fernet example")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(800, 400))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.key_tab = QWidget()
        self.key_tab.setObjectName(u"key_tab")
        self.key_generate_button = QPushButton(self.key_tab)
        self.key_generate_button.setObjectName(u"key_generate_button")
        self.key_generate_button.setGeometry(QRect(40, 230, 261, 71))
        self.key_input_button = QPushButton(self.key_tab)
        self.key_input_button.setObjectName(u"key_input_button")
        self.key_input_button.setGeometry(QRect(40, 100, 371, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.key_input_button.sizePolicy().hasHeightForWidth())
        self.key_input_button.setSizePolicy(sizePolicy1)
        self.exist_key_editor = QTextEdit(self.key_tab)
        self.exist_key_editor.setObjectName(u"exist_key_editor")
        self.exist_key_editor.setGeometry(QRect(40, 30, 641, 31))
        self.generated_key_editor = QTextEdit(self.key_tab)
        self.generated_key_editor.setObjectName(u"generated_key_editor")
        self.generated_key_editor.setGeometry(QRect(350, 230, 411, 71))
        self.tabWidget.addTab(self.key_tab, "")
        self.encrypt_tab = QWidget()
        self.encrypt_tab.setObjectName(u"encrypt_tab")
        self.encrypt_button = QPushButton(self.encrypt_tab)
        self.encrypt_button.setObjectName(u"encrypt_button")
        self.encrypt_button.setGeometry(QRect(280, 290, 171, 41))
        self.encrypt_input_editor = QTextEdit(self.encrypt_tab)
        self.encrypt_input_editor.setObjectName(u"encrypt_input_editor")
        self.encrypt_input_editor.setGeometry(QRect(10, 40, 351, 221))
        self.label_2 = QLabel(self.encrypt_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 63, 20))
        self.label_3 = QLabel(self.encrypt_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 121, 20))
        self.encrypt_output_editor = QTextEdit(self.encrypt_tab)
        self.encrypt_output_editor.setObjectName(u"encrypt_output_editor")
        self.encrypt_output_editor.setGeometry(QRect(370, 40, 391, 221))
        self.label_4 = QLabel(self.encrypt_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 10, 141, 20))
        self.tabWidget.addTab(self.encrypt_tab, "")
        self.decrypt_tab = QWidget()
        self.decrypt_tab.setObjectName(u"decrypt_tab")
        self.label_5 = QLabel(self.decrypt_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 131, 20))
        self.decrypt_input_editor = QTextEdit(self.decrypt_tab)
        self.decrypt_input_editor.setObjectName(u"decrypt_input_editor")
        self.decrypt_input_editor.setGeometry(QRect(10, 40, 351, 221))
        self.decrypt_output_editor = QTextEdit(self.decrypt_tab)
        self.decrypt_output_editor.setObjectName(u"decrypt_output_editor")
        self.decrypt_output_editor.setGeometry(QRect(370, 40, 391, 221))
        self.label_6 = QLabel(self.decrypt_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 10, 131, 20))
        self.decrypt_button = QPushButton(self.decrypt_tab)
        self.decrypt_button.setObjectName(u"decrypt_button")
        self.decrypt_button.setGeometry(QRect(280, 290, 171, 41))
        self.tabWidget.addTab(self.decrypt_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fernet example", None))
        self.key_generate_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.key_input_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u043a\u043b\u044e\u0447 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.generated_key_editor.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0443\u0442 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.key_tab), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.encrypt_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encrypt_tab), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.decrypt_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decrypt_tab), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

