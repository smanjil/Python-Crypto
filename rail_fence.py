#!/usr/bin/env python

import math
def get_message():
    message = raw_input("Enter message : ")
    get_key(message)

def get_key(message):
    key = input("Enter the depth : ")
    mode = raw_input("Enter E/e for encryption and D/d for decryption : ")
    helper(message , key , mode)

def helper(message , key , mode):
    space_li = ""
    for char in message:
        if ord(char) >= 97 and ord(char) <= 122:
	    space_li += char
    print space_li
    #length = len(space_li)
    #div = float(length) / float(key)
    #no_of_rows = math.ceil(div)
    i = 0
    mod = ""
    rem = ""
    remm = ""
    cipher = ""
    #print mode
    if mode == 'E' or mode == 'e':
        for char in space_li:        
            if i < len(space_li): 
                if i % key == 0:
                    mod += char
                elif i % key == 1:
                    rem += char
                else:
                    remm += char
            i += 1
        cipher = mod + rem + remm  
        print cipher
    elif mode == 'D' or mode == 'd':
        for char in space_li:        
            if i < len(space_li): 
                if i % key == 0:
                    mod += char
                elif i % key == 1:
                    rem += char
                else:
                    remm += char
            i += 1
        cipher = mod + rem + remm  
        print cipher
    else:
        print "Wrong choice!!!!"
           
get_message()


'''
a = []
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(i + j)
print a
'''


