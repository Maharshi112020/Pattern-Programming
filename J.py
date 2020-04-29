# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:42:46 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_J1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(row==0) or (row==h-1 and col<=w//2) or (col==w//2):
                print(p,end='')
            else:
                print(end=' ')
        print()

if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_J1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('Letter_height and Letter_width must be grater then 2')