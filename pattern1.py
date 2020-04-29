# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:08:17 2019

@author: Maharshi
"""

#   * 
#   * * * 
#   * * * * * 
#   * * * * * * * 
#   * * * * * * * * * 
import time
def pattern2(n,p):
    for i in range(n):
        for j in range((2*i)+1):
            print(p,end=' ')
        print()


def pattern2_single(n,p):
    for i in range(n):
        print((p+' ')*(2*i+1))

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern2(lines,p)
print(time.time() - t1)
print()
t2 = time.time()
pattern2_single(lines,p)
print(time.time() - t2)
