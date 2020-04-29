# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:51:01 2019

@author: Maharshi
"""

#       1
#      212
#     32123
#    4321234
#   543212345

n = int(input("Enter number of rows : "))
s = n
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()
