import math
import os

def main():
    y = 0
    public_key=input("Enter public key of receiver")
    y = int(sin(public_key*public_key)*10000000)
    if y<0:
        y = y*-1
    print(y)
    x = input("enter message")
    for i in y:
        for z in len(i):
            if(z+1 < len(x)):
                x[i] = x[i]+x[i+1]
            else:
                x[i] = x[i]+x[0]
    print(x)
