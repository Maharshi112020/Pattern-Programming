# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:34:57 2019

@author: Maharshi
"""

n = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")


#   *
#   **
#   ***
#   ****
#   *****
for i in range(1,n+1):
    print(p*i)


#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * * 
for i in range(1,n+1):
    for j in range(i):
        print(p,end=' ')
    print()
