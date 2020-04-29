# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:59:22 2019

@author: Maharshi
"""


#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * * 
import time
def pattern1(n,p):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(p,end=' ')
        print()
    

def pattern1_single(n,p):
    for i in range(1,n+1):
        print((p+' ')*i)
    

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern1(lines,p)
print(time.time()-t1)
print()
t2 = time.time()
pattern1_single(lines,p)
print(time.time() - t2)
