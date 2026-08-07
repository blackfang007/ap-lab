# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:53:08 2026

@author: maths
"""

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


while True:
    dec = int(input("Enter a Decimal Number: "))

    if dec == 0:
        print("\nBinary Equivalent: 0")
    else:
        print(f"\nBinary Equivalent: {decimal_to_binary(dec)}")

    choice = input("\Convert another number? (Y/N): ").strip().upper()
    print()

    if choice != "Y":
        break
