# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:10:24 2019

@author: Maharshi
"""

#Pyramid shape
#               1     
#            2     3     
#         4     5     6     
#      7     8     9     10    
#   11    12    13    14    15  

n = int(input("Enter the number of rows : "))
x = 1
for i in range(n):
    print(format(" ","<3")*(n-i-1),end='')
    for j in range(i+1):
        print(format(x,"<6"),end='')
        x += 1
    print()
        
    
