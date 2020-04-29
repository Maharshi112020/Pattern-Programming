# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:42:15 2019

@author: Maharshi
"""
#   numbers in rectangular triangle in zigzag fashion
#   1   
#   2   9   
#   3   8   10  
#   4   7   11  14  
#   5   6   12  13  15  

n = int(input("Enter the number of rows : "))

for i in range(n):
    for j in range(i+1):
        x = 0
        for k in range(j):
            x = x+n-k
        if(j%2==0):
            print(format(x+i-j+1,"<3"),end=' ')
        else:
            print(format(x+n-i,"<3"),end=' ')
    print()
