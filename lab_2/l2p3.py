# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:50:44 2026

@author: maths
"""

def calculateBill(*prices):
    if not prices:
        return 0, 0, 0, 0, 0, 0, 0
    
    total_items = len(prices)
    total_purchase = sum(prices)
    avg_price = total_purchase / total_items
    highest_price = max(prices)
    lowest_price = min(prices)
    
    discount_percentage = 0
    if total_purchase > 10000:
        discount_percentage = 0.15
    elif total_purchase > 5000:
        discount_percentage = 0.10
    elif total_purchase > 2000:
        discount_percentage = 0.05
        
    discount = total_purchase * discount_percentage
    amount_after_discount = total_purchase - discount
    gst = amount_after_discount * 0.18
    net_bill = amount_after_discount + gst
    
    return total_items, total_purchase, avg_price, highest_price, lowest_price, discount, gst, net_bill

print("SUPERMARKET BILLING SYSTEM")
name = input("Enter Customer Name : ")
num_items = int(input("Enter Number of Items : "))

item_prices = []
for i in range(num_items):
    price = float(input(f"Enter Price of Item {i+1}: ₹"))
    item_prices.append(price)

t_items, t_purchase, avg_p, high_p, low_p, disc, gst_amt, net_amt = calculateBill(*item_prices)

print("\nCUSTOMER BILL")
print(f"Total Items : {t_items}")
print(f"Total Purchase : ₹ {t_purchase:.1f}")
print(f"Average Item Price : ₹ {avg_p:.1f}")
print(f"Highest Price : ₹ {high_p:.1f}")
print(f"Lowest Price : ₹ {low_p:.1f}")
print(f"Discount : ₹ {disc:.1f}")
print(f"GST (18%) : ₹ {gst_amt:.1f}")
print(f"Net Bill Amount : ₹ {net_amt:.1f}")
