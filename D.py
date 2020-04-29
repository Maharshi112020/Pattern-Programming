# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:12:28 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_D1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(row==0 or row==h-1) or (row>0 and (col==0 or col==w-1)):
                print(p,end='')
            else:
                print(end=' ')
        print()
        
def print_D2(h,w,p):
    for row in range(h):
        for col in range(w):
            if((row==0 or row==h-1) and (col!=w-1)) or (0<row<h-1 and (col==0 or col==w-1)):
                print(p,end='')
            else:
                print(end=' ')
        print()

if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_D1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
    print()
    t2 = time.time()
    print_D2(letter_height,letter_width,pattern)
    print()
    print(time.time() - t2)
else:
    print('Letter_height and Letter_width must be grater then 2')