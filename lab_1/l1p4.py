# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:08:08 2026

@author: maths
"""

while True:
    print("=" * 36)
    print("      ELECTRICITY BILLING SYSTEM     ")
    print("=" * 36)

    name = input("Enter Consumer Name: ")
    if name == "":
        print("Error: Name cannot be empty.")
        continue

    consumer_num = input("Enter Consumer Number: ")
    if consumer_num == "":
        print("Error: Consumer number cannot be empty.")
        continue

    
    prev_str = input("Enter Previous Meter Reading: ")
    curr_str = input("Enter Current Meter Reading: ")
    age_str = input("Enter Consumer Age: ").strip()

    
    if not prev_str.isdigit() or not curr_str.isdigit() or not age_str.isdigit():
        print("Error: Please enter valid positive whole numbers.")
        continue

    prev_reading = float(prev_str)
    curr_reading = float(curr_str)
    age = int(age_str)

    if curr_reading < prev_reading:
        print("Error: Current reading must be greater than or equal to previous reading.")
        continue

    if age <= 0:
        print("Error: Age must be greater than zero.")
        continue

    units = curr_reading - prev_reading
    energy_charge = 0
    temp_units = units

    if temp_units > 500:
        energy_charge += (temp_units - 500) * 8
        temp_units = 500
    if temp_units > 300:
        energy_charge += (temp_units - 300) * 6
        temp_units = 300
    if temp_units > 100:
        energy_charge += (temp_units - 100) * 4
        temp_units = 100
    energy_charge += temp_units * 2

    fixed_charge = 100
    bill_before_discount = energy_charge + fixed_charge
    
    discount = 0.0
    if age >= 60:
        discount = bill_before_discount * 0.10

    bill_after_discount = bill_before_discount - discount
    
    rebate = 0.0
    if bill_after_discount > 5000:
        rebate = 500.0

    taxable_amount = bill_after_discount - rebate
    gst = taxable_amount * 0.18
    net_bill = taxable_amount + gst

    print("=" * 36)
    print("           ELECTRICITY BILL          ")
    print("=" * 36)
    print(f"Consumer Name          : {name}")
    print(f"Consumer Number        : {consumer_num}")
    print(f"Units Consumed         : {units:.0f}")
    print(f"Energy Charge          : ₹ {energy_charge:.2f}")
    print(f"Fixed Charge           : ₹ {fixed_charge:.2f}")
    print(f"Senior Citizen Discount: ₹ {discount:.2f}")
    print(f"Rebate                 : ₹ {rebate:.2f}")
    print(f"GST (18%)              : ₹ {gst:.2f}")
    print("-" * 36)
    print(f"Net Bill Amount        : ₹ {net_bill:.2f}")
    print("=" * 36)

    choice = input("Generate another bill? (Y/N): ").strip().upper()
    if choice != "Y":
        break
