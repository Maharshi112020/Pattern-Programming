# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:10:13 2019

@author: Maharshi
"""

#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 


import time

def pattern6(n,p):
    for i in range(n):
        print(' '*(n-i-1)+(p+' ')*(i+1))
    for j in range(n-1,0,-1):
        print(' '*(n-j)+(p+' ')*j)

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern6(lines,p)
print(time.time() - t1)
