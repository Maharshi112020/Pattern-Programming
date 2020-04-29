# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:53:38 2019

@author: Maharshi
"""
#
#   1 
#   2 3 
#   4 5 6 
#   7 8 9 10 
#   11 12 13 14 15 

n = int(input("Enter number of rows"))

a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=' ')
        a+=1
    print()
