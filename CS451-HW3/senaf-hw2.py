#Fred Sena  2-10-17
#CS 451 Homework 2

from Crypto.Cipher import DES #Imports pycrypto
import random

def cipher1(string1):

    while len(string1) % 8 != 0: #If string1 mod 8 does not equal zero, add in empty spaces
        string1 = string1 + " "

    key = ""
    for i in range(0,8):
        key = key + str(random.randint(0,9)) #Creates a random key 

    cipher = DES.new(key, DES.MODE_ECB) 

    ciph = cipher.encrypt(string1) #Encrypts the string
    return ciph



print "Welcome to the cipher function!\n"

string1 = raw_input('Please enter in a string to cipher: ')

print cipher1(string1)