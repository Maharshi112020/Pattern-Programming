# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:09:02 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_S1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(row==0 and col!=0) or (row==h-1 and col!=w-1) or (0<row<h//2 and col==0) or (h//2<row<h-1 and col==w-1) or (row==h//2 and 0<col<w-1):
                print(p,end='')
            else:
                print(end=' ')
        print()


if(letter_height>4 and letter_width>4):
    t1 = time.time()
    print_S1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('Letter_height and Letter_width must be grater then 4')