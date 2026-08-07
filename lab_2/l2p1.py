# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:15:24 2026

@author: maths
"""

import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"
def modulus(x, y): return x % y if y != 0 else "Error"
def power(x, y): return x ** y
def squareRoot(x): return math.sqrt(x) if x >= 0 else "Error"
def factorial(x): return math.factorial(int(x)) if x >= 0 else "Error"

while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Pow 7.Sqrt 8.Fact 9.Exit")
    choice = input("Choice: ")
    if choice == '9': break
    
    if choice in ('1', '2', '3', '4', '5', '6'):
        a, b = float(input("N1: ")), float(input("N2: "))
        ops = {'1':add, '2':subtract, '3':multiply, '4':divide, '5':modulus, '6':power}
        print("Result:", ops[choice](a, b))
    elif choice in ('7', '8'):
        n = float(input("N: "))
        print("Result:", squareRoot(n) if choice == '7' else factorial(n))
