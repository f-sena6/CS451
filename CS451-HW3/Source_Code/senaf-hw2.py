#Fred Sena  2-10-17
#CS 451 Homework 2

from Crypto.Cipher import DES #Imports pycrypto
import random

def encrypt_string(string1):

    while len(string1) % 8 != 0: #If string1 mod 8 does not equal zero, add in empty spaces
        string1 = string1 + " "

    key = "" #Creates the key
    for i in range(0,8):
        key = key + str(random.randint(0,9)) #Creates a random key 

    cipher = DES.new(key, DES.MODE_ECB) #DES Method used

    ciph = cipher.encrypt(string1) #Encrypts the string
    decrypted = cipher.decrypt(ciph) #Decrypts the string

    print "ENCRYPTED ==> ", ciph
    print "\n"
    print "DECRYPTED ==> ", decrypted



print "Welcome to the cipher function!\n"

string1 = raw_input('Please enter in a string to cipher: ')

encrypt_string(string1)
