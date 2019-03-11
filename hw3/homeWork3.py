"""
Created by: Jonathan J. Quintero Ramos
For: Cst205, Wes, homework3 3/10/19
~~~~~The Following code~~~~~~~~
Will take on the images from the file Images and the 
given dictionary to search and display the correct image
when searched for the closest match. This uses PyQt5 
for widget creation and Pillow for image management and 
displaying.
"""
#The following modules are required
# |
# V
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton,QVBoxLayout,QMainWindow, QLineEdit)
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, Qt

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon

import glob

from PIL import Image
#The following is the dictionary provided to search within 
#a match for image displaying
# |
# V
image_info = [
             {
                 "id" : "34694102243_3370955cf9_z",
                 "title" : "Eastern",
                 "flickr_user" : "Sean Davis",
                 "tags" : ["Los Angeles", "California", "building"]
                       },
             {
                 "id" : "37198655640_b64940bd52_z",
                 "title" : "Spreetunnel",
                 "flickr_user" : "Jens-Olaf Walter",
                 "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
                       },
             {
                 "id" : "36909037971_884bd535b1_z",
                 "title" : "East Side Gallery",
                 "flickr_user" : "Pieter van der Velden",
                 "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
                       },
             {
                 "id" : "36604481574_c9f5817172_z",
                 "title" : "Lombardia, september 2017",
                 "flickr_user" : "Mónica Pinheiro",
                 "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
                       },
             {
                 "id" : "36885467710_124f3d1e5d_z",
                 "title" : "Palazzo Madama",
                 "flickr_user" : "Kevin Kimtis",
                 "tags" : [ "Rome", "Italy", "window", "road", "building"]
                       },
             {
                 "id" : "37246779151_f26641d17f_z",
                 "title" : "Rijksmuseum library",
                 "flickr_user" : "John Keogh",
                 "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
                       },
             {
                 "id" : "36523127054_763afc5ed0_z",
                 "title" : "Canoeing in Amsterdam",
                 "flickr_user" : "bdodane",
                 "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
                       },
             {
                 "id" : "35889114281_85553fed76_z",
                 "title" : "Quiet at dawn, Cabo San Lucas",
                 "flickr_user" : "Erin Johnson",
                 "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
                       },
             {
                 "id" : "34944112220_de5c2684e7_z",
                 "title" : "View from our rental",
                 "flickr_user" : "Doug Finney",
                 "tags" : ["Mexico", "ocean", "beach", "palm"]
                       },
             {
                     "id" : "36140096743_df8ef41874_z",
                     "title" : "Someday",
                     "flickr_user" : "Thomas Hawk",
                     "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
                           }
             ]

#The following gets the images from the file Images and places
#them on a list named imageDict, it was a dictionary previously.
# |
# V
img = glob.glob("Images/*.jpg")
imageDict=[]
for i in img:
    imageDict.append(Image.open(i))

#The following is the location of the widget and overall functionality
# |
# V
class Log(QWidget):
    #The following initializes the speficied class initUI
    # |
    # V
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #The following is the creation of the widget with a lineEdit
        #and a Qcombobox. The qcombobox allow for image filters and activate
        #those filters
        # |
        # V
        self.input = QLineEdit()
        self.combo = QComboBox()
        self.lbl1 = QLabel("Input below",self)
        self.button = QPushButton("To search!")
        #The following activates a point based function to find the most matches.
        #The string value of the qcombobox is passed as well
        # |
        # V
        self.button.clicked.connect(self.comboActivated)
        
        self.combo.addItem("sepia")
        self.combo.addItem("negative")
        self.combo.addItem("grayscale")
        self.combo.addItem("thumbnail")
        self.combo.addItem("none")

        vbox = QVBoxLayout()

        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.input)
        vbox.addWidget(self.combo)
        vbox.addWidget(self.button)
        
        self.setLayout(vbox)
        self.setWindowTitle("Image Seach")
        #Shows the widget
        # |
        # V
        self.show()

    def comboActivated(self):
        text = self.combo.currentText()
        print(text)
        #Creation of the point system starts at zero every activation. 
        # |
        # V
        points = [0,0,0,0,0,0,0,0,0,0]
        #The following for loop goes through image_info dictionary to find
        #matches with a litera at the title as well as to the tags using the
        #self.input.text() to obtain the qline's text
        # |
        # V
        for i in range(len(image_info)):
            if(image_info[i]["title"]==self.input.text()):
                points[i]+=100
            for z in range(len(image_info[i]["tags"])):
                if(image_info[i]["tags"][z]==self.input.text()):
                    points[i]+=1
        #The following lines search for the index of the most matches, max is used
        #to determine what is the max amount of points found. once the first max 
        #match is found it is used to activate the chooserChange function with the 
        #qcombobox text value
        # |
        # V
        picker = max(points)
        thisOne = 0
        for i in range(len(points)):
            if(points[i]==picker):
                thisOne=i
                break
        if picker==0:
            print("ooof, try again")
        else:
            self.chooserChange(text,thisOne)
    
    #The following function uses if statements to find the corresponding filter
    # |
    # V
    def chooserChange(self, text, num):
        if(text=="none"):
            self.noneChange(num)
        if(text=="sepia"):
            self.sepiaChange(num)
        if(text=="negative"):
            self.negativeChange(num)
        if(text=="grayscale"):
            self.grayscaleChange(num)
        if(text=="thumbnail"):
            self.thumbnailChange(num)
    #The thumbnail filter simply takes half the image and uses it to make a new 
    #image of half the size. a simple for loop places the pixels the image is 
    #then displayed, num is the image in the Images file
    # |
    # V
    def thumbnailChange(self,num):
        im = imageDict[num]
        mi = Image.new("RGB", (int(im.width/2), int(im.height/2)))
        for x in range(int(im.width/2)):
            for y in range(int(im.height/2)):
                    red,green,blue = im.getpixel((x,y))
                    newcolor=((red),
                            (green),
                            (blue))
                    mi.putpixel((x,y), newcolor)
        mi.show()
    #The grayscale filter takes the original image's pixel values and then averages
    #the the tuple's values to then place the average for the rgb tuple. for loops
    #were used to place the pixel values to the new image and then display it
    # |
    # V
    def grayscaleChange(self,num):
        im = imageDict[num]
        mi = Image.new("RGB", (im.width, im.height))
        for x in range(im.width):
            for y in range(im.height):
                red,green,blue = im.getpixel((x,y))
                rgbMono = int((red+green+blue)/3)
                newcolor = ((rgbMono),
                            (rgbMono),
                            (rgbMono))
                mi.putpixel((x,y), newcolor)
        mi.show()
    #The negative filter takes the original image's pixel values and then subtracts
    #the tuple's values by 255 then places the rgb tuple. for loops were used to
    #place the pixel values to the new image and then display it
    # |
    # V
    def negativeChange(self,num):
        im = imageDict[num]
        mi = Image.new("RGB", (im.width, im.height))
        for x in range(im.width):
            for y in range(im.height):
                red,green,blue = im.getpixel((x,y))
                newcolor = (int(255-red),
                            int(255-green),
                            int(255-blue))
                mi.putpixel((x,y), newcolor)
        mi.show()
    #The sepia filter takes the original image's pixel values and then multiplies
    #the tuple's values ,correspondigly to the rgb values, then places the rgb tuple.
    #to a new image for loops were used to place the pixel values to the new 
    #image and then display it
    # |
    # V
    def sepiaChange(self,num):
        im = imageDict[num]
        mi = Image.new("RGB", (im.width,im.height))
        for x in range(im.width):
            for y in range(im.height):
                red,green,blue = im.getpixel((x,y))
                newcolor = (int(red *.5),
                            int(green *.3),
                            int(blue *.1))
                mi.putpixel((x,y), newcolor)
        mi.show()
    #The following literally displays the corresponding image from the image list    
    # |
    # V
    def noneChange(self,num):
        #print(num)
        im = imageDict[num]
        im.show()

#The following activates the class
# |
# V
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Log()
    sys.exit(app.exec_())

