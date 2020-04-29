# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:51:31 2019

@author: Maharshi
"""
#   1 
#   2 6 
#   3 7 10 
#   4 8 11 13 
#   5 9 12 14 15 

n = int(input("Enter the number of rows : "))

for row in range(n):
    val = row+1
    change = n-1
    for col in range(row+1):
        print(val,end=' ')
        val += change
        change -= 1
    print()
        
