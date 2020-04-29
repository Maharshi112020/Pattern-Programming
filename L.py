# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 00:01:21 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_L1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(col==0) or (row==h-1):
                print(p,end='')
            else:
                print(end=' ')
        print()


if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_L1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('Letter_height and Letter_width must be grater then 2')