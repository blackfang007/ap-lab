# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:59:00 2026

@author: maths
"""


rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    
    print("*" * i, end="")
    print(" " * (2 * (rows - i)), end="")
    print("*" * i)

for i in range(rows, 0, -1):
    
    print("*" * i, end="")
    print(" " * (2 * (rows - i)), end="")
    print("*" * i)
