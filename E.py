# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:34:31 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_E1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(col==0) or (col>0 and (row==0 or row==h//2 or row==h-1)):
                print(p,end='')
            else:
                print(end=' ')
        print()
        
def print_E2(h,w,p):
    for row in range(h):
        for col in range(w):
            if(col==0 and (row!=0 and row!=h//2 and row!=h-1)) or (col>0 and (row==0 or row==h//2 or row==h-1)):
                print(p,end='')
            else:
                print(end=' ')
        print()

if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_E1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
    print()
    t2 = time.time()
    print_E2(letter_height,letter_width,pattern)
    print()
    print(time.time() - t2)
else:
    print('Letter_height and Letter_width must be grater then 2')