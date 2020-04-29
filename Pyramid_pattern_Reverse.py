# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:53:31 2019

@author: Maharshi
"""

#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 

import time

def pattern5(n,p):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for j in range(i):
            print(p,end=' ')
        print()

def pattern5_single(n,p):
    for i in range(n,0,-1):
        print(' '*(n-i)+(p+' ')*i)

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern5(lines,p)
print(time.time() - t1)
print()
t2 = time.time()
pattern5_single(lines,p)
print(time.time() - t2)
