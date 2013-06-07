#!/usr/bin/python2.7
import sys 
import random
import os
from PyQt4 import QtGui,QtCore
from wndMain import Ui_wndMain as Wnd
from qotd import update_quotes_cache


class myWnd(QtGui.QMainWindow, Wnd): 
    def __init__(self):
        QtGui.QMainWindow.__init__(self) 
        self.setupUi(self)
        self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), quit)
        self.connect(self.btnGetQuote, QtCore.SIGNAL("clicked()"), self.onGetQuote)
        self.connect(self.btnGenerateImg, QtCore.SIGNAL("clicked()"), self.onGenerateImg)
        
    def onGenerateImg(self):
        FixedOptStr = '-colorspace gray +dither -colors 2 -gravity center -fill black '
        if self.chkLabel.isChecked():        
            Label = str(self.editLabel.toPlainText())
        else:
            Label = ''      
        LabelStr = '-font Times-Italic -size 320x240 xc:white caption:"' + Label + '"'
        CmdStr = 'convert ' + FixedOptStr + LabelStr + ' -composite out.bmp'
        print CmdStr
        os.system(CmdStr)
        print "Done"

    def onGetQuote(self):
        try:    
            self.editLabel.setPlainText(str(random.choice(update_quotes_cache())))
        except:
            self.editLabel.setPlainText("Error: " + str(sys.exc_info())) 
        
        

app = QtGui.QApplication(sys.argv) 
dialog = myWnd() 
dialog.show() 
sys.exit(app.exec_())
