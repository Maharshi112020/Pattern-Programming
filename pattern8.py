# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:01:21 2019

@author: Maharshi
"""

#       *
#      *A*
#     *A*A*
#    *A*A*A*
#   *A*A*A*A*

n = int(input("Enter the number of rows : "))
p1 = input("Enter the first pattern style : ")
p2 = input("Enter the second pattern style : ")

for i in range(n):
    print(' '*(n-i-1),end='')
    count = 0
    for j in range(i+1):
        print(p1,end='')
        if(count<i):
            print(p2,end='')
            count += 1
    
    print()
