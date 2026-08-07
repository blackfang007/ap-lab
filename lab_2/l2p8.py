# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:25:03 2026

@author: maths
"""

total_seats = 50

while total_seats > 0:
    
    print("RAILWAY RESERVATION SYSTEM")
    
    print("1. Book Ticket")
    print("2. View Available Seats")
    print("3. Exit")
    
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        name = input("Passenger Name : ")
        age = int(input("Age : "))
        gender = input("Gender (M/F) : ")
        
        print("Travel Classes")
        print("1. Sleeper")
        print("2. AC 3 Tier")
        print("3. AC 2 Tier")
        print("4. AC First Class")
        class_choice = int(input("Select Class : "))
        
        tickets = int(input("Number of Tickets : "))
        
        if tickets <= total_seats:
            if class_choice == 1:
                class_name = "Sleeper"
                base_fare = 200
            elif class_choice == 2:
                class_name = "AC 3 Tier"
                base_fare = 350
            elif class_choice == 3:
                class_name = "AC 2 Tier"
                base_fare = 500
            else:
                class_name = "AC First Class"
                base_fare = 650
                
            raw_fare = base_fare * tickets
            
            if age < 5:
                discount = raw_fare
            elif age >= 60:
                discount = raw_fare * 0.4
            else:
                discount = 0.0
                
            after_discount = raw_fare - discount
            gst = after_discount * 0.05
            total_amount = after_discount + gst
            
            total_seats = total_seats - tickets
            status = "Confirmed"
            
            
            print("BOOKING CONFIRMED")
            
            print("Passenger Name :", name)
            print("Age :", age)
            print("Gender :", gender)
            print("Travel Class :", class_name)
            print("Number of Tickets :", tickets)
            print("Ticket Fare : ₹", raw_fare)
            print("Discount : ₹", discount)
            print("GST (5%) : ₹", gst)
            print("Total Amount : ₹", total_amount)
            print("Booking Status :", status)
            print("Remaining Seats :", total_seats)
           
        else:
            
            print("NOT AVAILABLE - Insufficient Seats")
            
            
    elif choice == 2:
        print("Available Seats :", total_seats)
        
    elif choice == 3:
        break
