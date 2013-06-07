# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wndMain.ui'
#
# Created: Fri Jun  7 01:20:20 2013
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
        wndMain.resize(552, 459)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wndMain.sizePolicy().hasHeightForWidth())
        wndMain.setSizePolicy(sizePolicy)
        wndMain.setMinimumSize(QtCore.QSize(400, 300))
        wndMain.setMaximumSize(QtCore.QSize(700, 700))
        self.centralwidget = QtGui.QWidget(wndMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnExit = QtGui.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(450, 420, 87, 27))
        self.btnExit.setDefault(True)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 120, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.chkBitmap = QtGui.QCheckBox(self.centralwidget)
        self.chkBitmap.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.chkBitmap.setObjectName(_fromUtf8("chkBitmap"))
        self.graphBackground = QtGui.QGraphicsView(self.centralwidget)
        self.graphBackground.setGeometry(QtCore.QRect(10, 40, 106, 80))
        self.graphBackground.setObjectName(_fromUtf8("graphBackground"))
        self.btnBackground = QtGui.QToolButton(self.centralwidget)
        self.btnBackground.setGeometry(QtCore.QRect(490, 40, 41, 25))
        self.btnBackground.setObjectName(_fromUtf8("btnBackground"))
        self.editBackground = QtGui.QLineEdit(self.centralwidget)
        self.editBackground.setGeometry(QtCore.QRect(120, 40, 361, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.editBackground.setFont(font)
        self.editBackground.setObjectName(_fromUtf8("editBackground"))
        self.chkLabel = QtGui.QCheckBox(self.centralwidget)
        self.chkLabel.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.chkLabel.setObjectName(_fromUtf8("chkLabel"))
        self.editLabel = QtGui.QPlainTextEdit(self.centralwidget)
        self.editLabel.setGeometry(QtCore.QRect(10, 170, 341, 91))
        self.editLabel.setObjectName(_fromUtf8("editLabel"))
        self.btnGetQuote = QtGui.QPushButton(self.centralwidget)
        self.btnGetQuote.setGeometry(QtCore.QRect(426, 170, 111, 27))
        self.btnGetQuote.setObjectName(_fromUtf8("btnGetQuote"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 270, 521, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.btnGenerateImg = QtGui.QPushButton(self.centralwidget)
        self.btnGenerateImg.setGeometry(QtCore.QRect(426, 300, 111, 27))
        self.btnGenerateImg.setObjectName(_fromUtf8("btnGenerateImg"))
        self.graphImg = QtGui.QGraphicsView(self.centralwidget)
        self.graphImg.setGeometry(QtCore.QRect(10, 290, 171, 111))
        self.graphImg.setInteractive(False)
        self.graphImg.setObjectName(_fromUtf8("graphImg"))
        wndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(wndMain)
        QtCore.QMetaObject.connectSlotsByName(wndMain)

    def retranslateUi(self, wndMain):
        wndMain.setWindowTitle(QtGui.QApplication.translate("wndMain", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("wndMain", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.chkBitmap.setText(QtGui.QApplication.translate("wndMain", "Bitmap background", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBackground.setText(QtGui.QApplication.translate("wndMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.editBackground.setText(QtGui.QApplication.translate("wndMain", "some filename", None, QtGui.QApplication.UnicodeUTF8))
        self.chkLabel.setText(QtGui.QApplication.translate("wndMain", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGetQuote.setText(QtGui.QApplication.translate("wndMain", "Generate quote", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGenerateImg.setText(QtGui.QApplication.translate("wndMain", "Generate image", None, QtGui.QApplication.UnicodeUTF8))

