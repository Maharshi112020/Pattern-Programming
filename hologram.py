# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:36:52 2019

@author: Maharshi
"""

#     *  
#    * * 
#   *   *
#    * * 
#     * 

n = int(input("Enter Hologram Size : "))
p = input("Enter Pattern Style : ")
x = n//2
for row in range(n):
    for col in range(n):
        if(row+col==x) or (col-row==x) or (row-col==x) or (row+col-x==n-1):
            print(p,end='')
        else:
            print(end=' ')
    print()
