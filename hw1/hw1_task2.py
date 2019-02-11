#Created by: Jonathan J. Quintero Ramos and Jesus "Chuy" Gomez
#finished on 2/09/2019
#Created for Cst205 professor Wes at CSUMB
#The following code uses pickle to de-serialize a pickled code (a serilzlized data)
#By looping through the file's data which is strored on a different variable
#This variable is then used by a function to see what intensities there are of the rgb colors of the image.
#it is then sent to another function in which an svg image of the data's histogram is created

import pickle 
# Part of python3 to deserialize data is imported, part of python3
import hw1_hist_plotter as hp
# The following was imported to use the data conversion of the function and generate the histogram.
def task2 (alpha, beta,firstImage):
    #The function uses alpha as the number of lists, beta for the number of tuples per list and firstImage as the de-pickled list generated from the data

    redBin = [0,0,0,0]

    greenBin = [0,0,0,0]
     
    blueBin =  [0,0,0,0]
    #The lists created set the four intensities for the rgb spectrum

    for x in range(alpha):
        #Loops through the lists available 
        for y in range(beta):
            #loops through the tuples in those lists
            for z in range(3):
                #loops through the tuple's data
                if z ==0:
                    #checks for the position of the data, as the 0 position is for the red pigment

                    if firstImage[x][y][z] <= 63:
                        redBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        redBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        redBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        redBin[3]+=1
                        
                        #The if statements then filter and adds to the correct intensity as a counter

                if z == 1:
                    #the 1 position of the tuple is for hte green tuple

                    if firstImage[x][y][z] <= 63:
                        greenBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        greenBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        greenBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        greenBin[3]+=1

                        #The if statements then filter and adds to the correct intensity as a counter

                if z == 2:
                    #The 2 position is for the green pigment

                    if firstImage[x][y][z] <= 63:
                        blueBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        blueBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        blueBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        blueBin[3]+=1

                        #The if statements then filter and adds to the correct intensity as a counter

    masterList = [redBin,greenBin,blueBin]
    #the lists are then placed on a master list

    print(masterList)
    # if there is a known amount already then printing the master list will verify that

    #masterList is then returned for usage by the histogram function
    return masterList

data = open('image_matrix','rb')
#To use the data the file containing must be opened with the rb reading attribute
newData = pickle.load(data)
#The data is then dezerialized and passed to a new variable for usage
data.close()
#once the data is stored on the new variable the file is close

first = len(newData)
#to use the function the number of lists must be first known
second = len(newData[0])
#the number of tuples per list must also be known

#task2(first,second,newData)
hp.hist_plotter(task2(first,second,newData))
#The function to make the histograms is then used with the function as part of its parametes
