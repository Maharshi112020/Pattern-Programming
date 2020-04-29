# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:56:10 2019

@author: Maharshi
"""

#   15  
#   14  10  
#   13  9   6   
#   12  8   5   3   
#   11  7   4   2   1  

n = int(input("Enter the number of rows : "))
k = (n*(n+1))//2
for row in range(n):
    val = k - row
    change = n-1
    for col in range(row+1):
        print(format(val,"<4"),end='')
        val -= change
        change -= 1
    print()
