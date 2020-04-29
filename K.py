# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:47:04 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_K1(h,w,p):
    i = 0
    j = w-1
    for row in range(h):
        for col in range(w):
            if(col==0) or (col>1 and row==col+2):
                print(p,end='')
            elif(row==i and col==j) and col>0:
                print(p,end='')
                i += 1
                j -= 1
            else:
                print(end=' ')
        print()

if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_K1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('Letter_height and Letter_width must be grater then 2')