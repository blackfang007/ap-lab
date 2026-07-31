# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:14:50 2026

@author: maths
"""

def find_prime_factors(number):
    
    
    factors = []
    
    
    divisor = 2
    
   
    while number > 1:
        
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor  
        else:
           
            divisor += 1
            
    return factors



if __name__ == "__main__":
        user_input = int(input("Enter a positive integer: "))
        
        if user_input <= 0:
            print("Please enter an integer greater than 0.")
        elif user_input == 1:
            print("The number 1 has no prime factors.")
        else:
            prime_factors = find_prime_factors(user_input)
            print(f"The prime factors of {user_input} are: {prime_factors}")
            
   
