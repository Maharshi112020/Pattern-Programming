# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:07:18 2019

@author: Maharshi
"""

#   Heart Shape
#    ** ** 
#   *  *  *
#   *     *
#    *   * 
#     * *  
#      * 

n = int(input("Enter the width of the heart : "))
p = input("Enter pattern style : ")
w = n
h = n-1
x = h//2 

#Empty Heart
for row in range(h):
    for col in range(w):
        if(row==0 and (col!=0 and col!=n//2 and col!=w-1)) or (row==1 and (col==0 or col==n//2 or col==w-1)) or (1<row<h//2 and (col==0 or col==w-1)) or (col<=w//2 and (row-col+1==x)) or (x<=row<h-1 and (row+col==h+x-1)):
            print(p,end='')
        else:
            print(end=' ')
    print()
