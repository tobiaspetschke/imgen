# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wndMain.ui'
#
# Created: Wed May 15 21:46:36 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_wndMain(object):
    def setupUi(self, wndMain):
        wndMain.setObjectName(_fromUtf8("wndMain"))
        wndMain.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wndMain.sizePolicy().hasHeightForWidth())
        wndMain.setSizePolicy(sizePolicy)
        wndMain.setMinimumSize(QtCore.QSize(400, 300))
        wndMain.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtGui.QWidget(wndMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnOK = QtGui.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(200, 250, 87, 27))
        self.btnOK.setDefault(True)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(300, 250, 87, 27))
        self.btnCancel.setDefault(True)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        wndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(wndMain)
        QtCore.QMetaObject.connectSlotsByName(wndMain)

    def retranslateUi(self, wndMain):
        wndMain.setWindowTitle(QtGui.QApplication.translate("wndMain", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOK.setText(QtGui.QApplication.translate("wndMain", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("wndMain", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

