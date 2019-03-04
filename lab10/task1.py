from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel("Please",self)
        self.lbl2 = QLabel("RGB: ",self)
        self.lbl3 = QLabel("Hex: ",self)
        self.lbl4 = QLabel("Please",self)
        combo = QComboBox(self)
        combo.addItem("Navy")
        combo.addItem("Teal")
        combo.addItem("Green")
        combo.addItem("Maroon")
        combo.addItem("Silver")
        combo.move(50,50)
        self.lbl1.move(75,150)
        self.lbl2.move(50,150)
        self.lbl3.move(150, 150)
        self.lbl4.move(175,150)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        if(text=="Navy"):
            self.lbl1.setText("(0,0,128)")
            self.lbl1.adjustSize()
            self.lbl4.setText("#000080")
            self.lbl4.adjustSize()

        if(text=="Teal"):
            self.lbl1.setText("(0,0,128)")
            self.lbl1.adjustSize()
            self.lbl4.setText("#008080")
            self.lbl4.adjustSize()

        if(text=="Green"):
            self.lbl1.setText("(0,128,0)")
            self.lbl1.adjustSize()
            self.lbl4.setText("#008000")
            self.lbl4.adjustSize()

        if(text=="Maroon"):
            self.lbl1.setText("(128,0,0)")
            self.lbl1.adjustSize()
            self.lbl4.setText("#800000")
            self.lbl4.adjustSize()
            
        if(text=="Silver"):
            self.lbl1.setText("(128,128,128)")
            self.lbl1.adjustSize()
            self.lbl4.setText("#C0C0C0")
            self.lbl4.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
