# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:23:37 2019

@author: Maharshi
"""

#   Spiral form of the square matrix
#   1       2       3       4       5       
#   16      17      18      19      6       
#   15      24      25      20      7       
#   14      23      22      21      8       
#   13      12      11      10      9 

#h = int(input("Enter height of matrix : "))
#w = int(input("Enter width of matrix : "))

n = int(input("Enter the dimension of square matrix : "))
low = 0
high = n-1
count = (n+1)//2
l = [[0 for x in range(n)] for y in range(n)]
a = 1
#printing number in square shape

for i in range(count):
    for j in range(low,high+1):
        l[i][j] = a
        a += 1
    for j in range(low+1,high+1):
        l[j][high] = a
        a += 1
    for j in range(high-1,low-1,-1):
        l[high][j] = a
        a += 1
    for j in range(high-1,low,-1):
        l[j][low] = a
        a += 1
    low += 1
    high -= 1
    
for i in range(n):
    for j in range(n):
        print(l[i][j],end='\t')
    print()
