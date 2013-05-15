import sys 
from PyQt4 import QtGui,QtCore
from wndMain import Ui_wndMain as Wnd

class myWnd(QtGui.QMainWindow, Wnd): 
    def __init__(self): 
        QtGui.QMainWindow.__init__(self) 
        self.setupUi(self)
        self.connect(self.btnOK, QtCore.SIGNAL("clicked()"), self.onOK)
        
    def onOK(self):
        self.close()
        

app = QtGui.QApplication(sys.argv) 
dialog = myWnd() 
dialog.show() 
sys.exit(app.exec_())
