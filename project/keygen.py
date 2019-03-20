import math
import os

def key(ID):
    public_key = int(cos(ID*ID) * 10000000)
    print("This is your publick key"+public_key)
    private_key = int(sin(public_key*public_key)*10000000)
    if(private_key<):
        private_key = private_key*-1
    print("this is your private key" + private_key)
    return public_key

def start ():
    u=input("enter the last five of your student ID or a five digit gen key")
    key(u)
    return int(cos(u*u)*10000000)

