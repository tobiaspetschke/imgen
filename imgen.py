#!/usr/bin/python2.7
import sys 
import random
from PyQt4 import QtGui,QtCore
from wndMain import Ui_wndMain as Wnd
from qotd import update_quotes_cache


class myWnd(QtGui.QMainWindow, Wnd): 
    def __init__(self):
        QtGui.QMainWindow.__init__(self) 
        self.setupUi(self)
        self.connect(self.btnExit, QtCore.SIGNAL("clicked()"), quit)
        self.connect(self.btnGetQuote, QtCore.SIGNAL("clicked()"), self.onGetQuote)
        
    def onGetQuote(self):
        try:    
            self.editLabel.setPlainText(str(random.choice(update_quotes_cache())))
        except:
            self.editLabel.setPlainText("Error: " + str(sys.exc_info())) 
        
        

app = QtGui.QApplication(sys.argv) 
dialog = myWnd() 
dialog.show() 
sys.exit(app.exec_())
