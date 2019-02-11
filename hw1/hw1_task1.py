#Created by: Jonathan J. Quintero Ramos and Jesus "Chuy" Gomez
#finished on 2/09/2019
#Created for Cst205 professor Wes at CSUMB
#The following code uses pickle to de-serialize a pickled code (a serilzlized code)
#By looping through the file's data which is strored on a different variable
#From this the color density is sorted by four equal sized intensities in which are stored in a dictionary and then displayed.

import pickle
#pickle is included with python3 and is just imported

#the following function will filter the information of the file and then cycle through the data and print it as dictionary 
def hw1 (alpha, beta,firstImage):
    #the parameters of the function are (alpha) for the file's list size, (beta) for the amount of tuples per list, and (firstImage) for the file's un-serialized data to be passed on.
    redBin = [0,0,0,0]

    greenBin = [0,0,0,0]
     
    blueBin =  [0,0,0,0]
    #the bins were created so that the intensities may be easily dealt with and later on added to the dictionary, also more colors can be created if so preferred and added to the dictionary at the end.


    for x in range(alpha):
        #To cycle through the lists
        for y in range(beta):
            #To cycle through the tuples in the lists
            for z in range(3):
                #To cycle through the tuple's data
                if z ==0:
                    #The the if statement checks for the data's tuple position, as the zero position is for the red pigment, one is green and two is blue.

                    #The if statements after check for the intensity and add as a counter to the correct intensity of the color
                    if firstImage[x][y][z] <= 63:
                        redBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        redBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        redBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        redBin[3]+=1

                if z == 1:
                    #for the green 

                    if firstImage[x][y][z] <= 63:
                        greenBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        greenBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        greenBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        greenBin[3]+=1

                if z == 2:
                    #for the blue 

                    if firstImage[x][y][z] <= 63:
                        blueBin[0]+=1

                    if firstImage[x][y][z] > 63 and firstImage[x][y][z] <= 127:
                        blueBin[1]+=1

                    if firstImage[x][y][z] > 127 and firstImage[x][y][z] <= 191:
                        blueBin[2]+=1

                    if firstImage[x][y][z] > 191 and firstImage[x][y][z] <= 255:
                        blueBin[3]+=1
    #here the data of the lists is added to a dictionary with the corresponding color key
    aDict = {"red": redBin,"green" : greenBin, "blue": blueBin}
    #the dictionary is printed then
    print(aDict)

#To dezerialize the data the file must be first opened with the rb reading typing for the pickle
data = open('image_matrix','rb')
newData = pickle.load(data)
#A new variable is then created to store the dezerialized data and then the file is closed
data.close()


#the following were to understand the size of the data
#print(len(newData))
#print(len(newData[1]))
#print(len(newData[0][0]))
#print(newData)

#To use the data correctly the size of the must be first inputted as the paramenters  
first = len(newData)
second = len(newData[0])

#The fucntion is then called.
hw1(first,second,newData)

