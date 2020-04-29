# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:29:17 2019

@author: Maharshi
"""

n = int(input("Enter Width of Triangle : "))
p = input("Enter Pattern Style : ")
w = n
h = n//2 + 1
x = n//2

#consecutive pattern in last row
#     *  
#    * * 
#   *****

for row in range(h):
    for col in range(w):
        if(row==h-1) or (row+col==x) or (col-row==x):
            print(p,end='')
        else:
            print(end=' ')
    print()
    
#alternative pattern in last row
#     *  
#    * * 
#   * * *
for row in range(h):
    for col in range(w):
        if(row==h-1 and col%2==0) or (row+col==x) or (col-row==x):
            print(p,end='')
        else:
            print(end=' ')
    print()
