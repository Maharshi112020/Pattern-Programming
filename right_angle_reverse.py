# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:27:59 2019

@author: Maharshi
"""

#   * * * * * 
#   * * * * 
#   * * * 
#   * * 
#   * 


import time

def pattern7(n,p):
    for i in range(n,0,-1):
        print((p+' ')*i)

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern7(lines,p)
print(time.time() - t1)
