#!/usr/bin/env python
import random
def password_generator():
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password= ""
    x= 0 
    while x <3: #To control the length of the password
        y=0
        while y<3: #To produce the first 3 characters before the hyphen
            password += random.choice(char)
            y+=1
        if len(password)<11:
            password+= "-"
        x+=1
    print(password)
password_generator()