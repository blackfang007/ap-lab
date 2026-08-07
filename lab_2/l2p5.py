# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:52:37 2026

@author: maths
"""

calc_gross = lambda basic, hra, da: basic + hra + da
calc_tax = lambda gross, tax_pct: gross * (tax_pct / 100)
calc_bonus = lambda gross: 5000.0
calc_net = lambda gross, tax, bonus: gross - tax + bonus

while True:
    print("      EMPLOYEE SALARY SYSTEM")
    name = input("Enter Employee Name : ")
    emp_id = input("Enter Employee ID   : ")
    
    basic = float(input("Enter Basic Salary : ₹"))
    hra = float(input("Enter HRA           : ₹"))
    da = float(input("Enter DA            : ₹"))
    tax_pct = float(input("Enter Tax (%)       : "))
    
    if basic <= 0 or hra < 0 or da < 0:
        print("Validation Error: Salary components must be greater than 0.")
        break
    if tax_pct > 30:
        print("Validation Error: Tax cannot be greater than 30%.")
        break
        
    gross = calc_gross(basic, hra, da)
    tax_amt = calc_tax(gross, tax_pct)
    bonus = calc_bonus(gross)
    net = calc_net(gross, tax_amt, bonus)
    
    print("          SALARY SLIP")
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {emp_id}")
    print(f"Basic Salary  : ₹ {basic:.1f}")
    print(f"HRA           : ₹ {hra:.1f}")
    print(f"DA            : ₹ {da:.1f}")
    print(f"Gross Salary  : ₹ {gross:.1f}")
    print(f"Tax Amount    : ₹ {tax_amt:.1f}")
    print(f"Bonus         : ₹ {bonus:.1f}")
    print(f"Net Salary    : ₹ {net:.1f}")
    
    choice = input("Process another employee? (Y/N): ").strip().upper()
    if choice != 'Y':
        break
