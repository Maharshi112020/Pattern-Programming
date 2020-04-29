# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:22:42 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_W1(h,w,p):
    for row in range(h):
        for col in range(w):
            if(row==col) or (row+col==w//2) or (col-row==w//2) or (row+col==w-1):
                print(p,end='')
            else:
                print(end=' ')
        print()


if(letter_height>letter_width//4):
    t1 = time.time()
    print_W1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('letter_height>letter_width//4')