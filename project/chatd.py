import math
import os

def decrypt(x, key):
    if(key<0):
        key = key*-1

    for i in range(key):
        while len(i)-1 >=0:
            if(i < len(x)-1):
                x[i] = x[i]-x[i-1]
            else:
                x[i] = x[i]-x[0]
    return x

#   Need Help with the Print function
#   Don't get the .is_open() method on python3

def print(w, key):
    fi = open(w+".txt")
    fil = fi.read()
    if(!fil):
        print("error please contaact room 707 between 4-6PM M-F")
    if(
