from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QPushButton,QVBoxLayout,QMainWindow, QLineEdit, QHBoxLayout
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
import sys,time
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QScrollBar,QSplitter,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread 
from socketserver import ThreadingMixIn 

class Start(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl1 = QLabel("Your name for today?")

        self.btn = QPushButton("Connect to person", self)
        self.btn2 = QPushButton("This name", self)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.textbox2)
        vbox.addWidget(self.btn2)
        
        vbox.addWidget(self.lbl1)
        self.setLayout(vbox)
        self.btn.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click_2)

        self.setWindowTitle('Encrpted Chat')
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        #self.displaySecond = secondWindow(self.textbox.text())
        #self.displaySecond.show()
        self.displaySecond = Window(self.textbox.text())
        self.displaySecond.show()

    def on_click_2(self):
        self.lbl1.setText(self.textbox2.text())
    
class Window(QDialog):
    def __init__(self, name):
        super().__init__()
        self.flag=0
        self.chatTextField=QLineEdit(self)
        self.chatTextField.resize(480,100)
        self.chatTextField.move(10,350)
        self.btnSend=QPushButton("Send",self)
        self.btnSend.resize(480,30)
        self.btnSendFont=self.btnSend.font()
        self.btnSendFont.setPointSize(15)
        self.btnSend.setFont(self.btnSendFont)
        self.btnSend.move(10,460)
        self.btnSend.setStyleSheet("background-color: #606060")
        self.btnSend.clicked.connect(self.send)
 
        self.chatBody=QVBoxLayout(self)
        # self.chatBody.addWidget(self.chatTextField)
        # self.chatBody.addWidget(self.btnSend)
        # self.chatWidget.setLayout(self.chatBody)
        splitter=QSplitter(QtCore.Qt.Vertical)
 
        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
 
        splitter.addWidget(self.chat)
        splitter.addWidget(self.chatTextField)
        splitter.setSizes([400,100])
 
        splitter2=QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter)
        splitter2.addWidget(self.btnSend)
        splitter2.setSizes([200,10])
 
        self.chatBody.addWidget(splitter2)
 
        self.setWindowTitle(name)
        self.resize(500, 500)

    def send(self):
        text=self.chatTextField.text()
        font=self.chat.font()
        font.setPointSize(13)
        self.chat.setFont(font)
        textFormatted='{:>80}'.format(text)
        self.chat.append(textFormatted)
        #global conn
        #conn.send(text.encode("utf-8"))
        self.chatTextField.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start() 
    sys.exit(app.exec_())
