import math
import os

def int2string(x):
    y=""
    z = ''
    while(x!=0):
        z=(x%10)+'0'
        x=x/10
        y=z+y
    return y

def encrypt(public_key):
    string x 
    y = int(sin(public_key*public_key)*10000000)
    if(y<0):
        y = y*-1
    x = input("enter message")
    for i in range(y-1):
        for i in range(x-1):
            if i+1 < len(x):
                x[i]=x[i]+x[i+1]
            else:
                x[i] = x[i]+x[0]
    p = int2string(public_key)
    fil = open(p+".txt",'w')
    #Need Help with the !write and stuff
    #do not know it at all.
    if(
