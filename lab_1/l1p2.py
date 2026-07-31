# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:37:12 2026

@author: maths
"""

import math

def classify_number(num):
    
    if num <= 0:
        return "Please enter a positive integer greater than 0."
        
    
    if num == 1:
        return "Deficient Number"

   
    divisors_sum = 1 
    square_root = int(math.sqrt(num))
    
   
    for i in range(2, square_root + 1):
        if num % i == 0:
            divisors_sum += i
            
            if i != num // i:
                divisors_sum += num // i

    
    if divisors_sum == num:
        return "Perfect Number"
    elif divisors_sum > num:
        return "Abundant Number"
    else:
        return "Deficient Number"
    
    


if __name__ == "__main__":
        user_input = int(input("Enter a positive integer: "))
        result = classify_number(user_input)
        print(f"The number {user_input} is a {result}.")
        
       
