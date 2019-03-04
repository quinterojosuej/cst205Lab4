from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton,QVBoxLayout,QMainWindow)
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
#from PyQt5.QtWebEngineWidgets import QWebEngineView

#from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import Qt

dictionary = {0:["Navy",(0,0,128),"#000080","(0,0,128)"],1:["Teal",(0,128,128),"#008080","(0,128,128)"],
        2:["Green",(0,128,0),"#008000","(0,128,0)"],3:["Maroon",(128,0,0),"#800000","(128,0,0)"],4:["Silver",(128,128,128),"#C0C0C0","(128,128,128)"]}



class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel("Please",self)
        self.lbl2 = QLabel("RGB: ",self)
        self.lbl3 = QLabel("Hex: ",self)
        self.lbl4 = QLabel("Please",self)
        self.btn = QPushButton("To color!", self)
        
        self.combo = QComboBox()

        self.combo.addItem("Navy")
        self.combo.addItem("Teal")
        self.combo.addItem("Green")
        self.combo.addItem("Maroon")
        self.combo.addItem("Silver")

        #self.combo.move(100,50)
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.lbl3)
        vbox.addWidget(self.lbl4)
        
        self.setLayout(vbox)
        self.btn.clicked.connect(self.on_click)

        self.combo.activated[str].connect(self.onActivated)
        #self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl1.setText(dictionary[self.combo.currentIndex()][3])
        self.lbl4.setText(dictionary[self.combo.currentIndex()][2])
    
    @pyqtSlot()
    def on_click(self):
        i = self.combo.currentIndex()
         
        self.displaySecond = secondWindow(dictionary[i][1])
        self.displaySecond.show()
    
class secondWindow(QWidget):
    def __init__(self, num):
        super().__init__()
        self.setGeometry(50,50,200,200)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(num[0],num[1],num[2]))
        self.setPalette(p)

class thirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.secondExample()
    def secondExample(self):
        self.setGeometry(50,50,200,200)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(0,0,0))
        self.setPalette(p)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example() 
    sys.exit(app.exec_())
