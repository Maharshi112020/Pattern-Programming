# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:23:38 2019

@author: Maharshi
"""

n = int(input("Enter number of rows : "))

#   1 2 3 4 5 
#   1 2 3 4 
#   1 2 3 
#   1 2 
#   1

for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
   
    
    
#   5 5 5 5 5 
#   4 4 4 4 
#   3 3 3 
#   2 2 
#   1 
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
    
