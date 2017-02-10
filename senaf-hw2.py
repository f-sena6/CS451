#Fred Sena  2-10-17
#CS 451 Homework 2

from Crypto.Cipher import DES
import random

def cipher1(hash1):

    while len(hash1) % 8 != 0:
        hash1 = hash1 + " "

    key = ""
    for i in range(0,8):
        key = key + str(random.randint(0,9))

    cipher = DES.new(key, DES.MODE_ECB)

    ciph = cipher.encrypt(hash1)
    return ciph



print "Welcome to the cipher function!\n"

string1 = raw_input('Please enter in a string to cipher: ')

print cipher1(string1)