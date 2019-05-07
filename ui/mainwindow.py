# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 674)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.ausgabe_label = QtWidgets.QLabel(self.centralWidget)
        self.ausgabe_label.setText("")
        self.ausgabe_label.setObjectName("ausgabe_label")
        self.gridLayout.addWidget(self.ausgabe_label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(9)
        self.formLayout.setVerticalSpacing(17)
        self.formLayout.setObjectName("formLayout")
        self.land_label = QtWidgets.QLabel(self.centralWidget)
        self.land_label.setAlignment(QtCore.Qt.AlignCenter)
        self.land_label.setObjectName("land_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.land_label)
        self.land_combo = QtWidgets.QComboBox(self.centralWidget)
        self.land_combo.setEditable(False)
        self.land_combo.setCurrentText("")
        self.land_combo.setMaxCount(2147483647)
        self.land_combo.setObjectName("land_combo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.land_combo)
        self.eigenschaft_label = QtWidgets.QLabel(self.centralWidget)
        self.eigenschaft_label.setAlignment(QtCore.Qt.AlignCenter)
        self.eigenschaft_label.setObjectName("eigenschaft_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.eigenschaft_label)
        self.eigenschaft_combo = QtWidgets.QComboBox(self.centralWidget)
        self.eigenschaft_combo.setObjectName("eigenschaft_combo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.eigenschaft_combo)
        self.ok = QtWidgets.QPushButton(self.centralWidget)
        self.ok.setObjectName("ok")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ok)
        self.abbr = QtWidgets.QPushButton(self.centralWidget)
        self.abbr.setObjectName("abbr")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.abbr)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.close_button = QtWidgets.QPushButton(self.centralWidget)
        self.close_button.setStyleSheet("")
        self.close_button.setObjectName("close_button")
        self.gridLayout.addWidget(self.close_button, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wikipedia"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.land_label.setText(_translate("MainWindow", "Country"))
        self.eigenschaft_label.setText(_translate("MainWindow", "Feature"))
        self.ok.setText(_translate("MainWindow", "OK"))
        self.abbr.setText(_translate("MainWindow", "Cancel"))
        self.close_button.setText(_translate("MainWindow", "Close"))


