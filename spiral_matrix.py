# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:47:37 2019

@author: Maharshi
"""
#   spiral form of any matrix

#   Enter height of the matrix : 6
#   
#   Enter width of the matrix : 3
#   1       2       3       
#   14      15      4       
#   13      16      5       
#   12      17      6       
#   11      18      7       
#   10      9       8  
h = int(input("Enter height of the matrix : "))
w = int(input("Enter width of the matrix : "))
row_min = 0
row_max = h
col_min = 0
col_max = w
n = 1
l = [[0 for x in range(w)] for y in range(h)]

while(row_min<row_max and col_min<col_max):
#    print first row from remaining matrix
    for i in range(col_min,col_max):
        l[row_min][i] = n
        n += 1
    row_min += 1
    
#    print last column from remaining matrix
    for i in range(row_min,row_max):
        l[i][col_max-1] = n
        n += 1
    col_max -= 1
    
#    print last row from remaining matrix
    if(row_min<row_max):
        for i in range(col_max-1,col_min-1,-1):
            l[row_max-1][i] = n
            n += 1
        row_max -= 1
    
#    print first column from remaining matrix
    if(col_min<col_max):
        for i in range(row_max-1,row_min-1,-1):
            l[i][col_min] = n
            n += 1
        col_min += 1
            
    
    
    
    
    
    
for i in l:
    for j in i:
        print(j,end='\t')
    print()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
