# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:53:08 2026

@author: maths
"""

from functools import reduce

while True:
    
    print("EMPLOYEE SALARY ANALYSIS")
    
    n = int(input("Enter Number of Employees : "))
    salaries = []
    for i in range(n):
        s = float(input(f"Enter Salary of Employee {i+1}: ₹"))
        salaries.append(s)
    
    above_50k = list(filter(lambda x: x > 50000, salaries))
    updated_salaries = list(map(lambda x: x * 1.1, salaries))
    total_expense = reduce(lambda x, y: x + y, updated_salaries)
    
   
    print("SALARY ANALYSIS REPORT")
    
    print(f"Original Salary List {salaries}")
    print(f"Employees Earning Above ₹50,000 {above_50k}")
    print(f"Updated Salary List (10% Increment) {updated_salaries}")
    print(f"Total Salary Expenditure ₹ {total_expense}")
    
    
    choice = input("Analyze another salary list? (Y/N): ").strip().upper()
    if choice != 'Y':
        break
    