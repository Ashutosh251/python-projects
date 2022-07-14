# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 05:48:20 2021

@author: Ashutosh Singh
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
l = nr_letters
s = nr_symbols
n = nr_numbers

for i in range(0,l):
    k = random.randint(0,len(letters)-1)
    password += letters[k]

for j in range(0,s):
    k1 = random.choice(symbols)
    password += k1
    
for c in range(0,n):
    k2 = random.choice(numbers)
    password += k2
print(password)

s_pass = ""
for o in range(0,len(password)):
    a = random.choice(password)
    s_pass += a
print(s_pass)
#or use random.shuffle() but for that first convert password into a list then use the shuffle function and convert it back to string using for