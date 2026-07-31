# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:24:41 2026

@author: maths
"""


stored_pin = "1234"
balance = 50000
attempts = 0
authenticated = False


while attempts < 3:
  entered_pin = input("Enter your 4-digit PIN : ")
  if entered_pin == stored_pin:
    authenticated = True
    print("Login Successful.")
    break
  else:
    attempts = attempts + 1
    print("Incorrect PIN. Try again.")

if authenticated == False:
  print("Account Blocked. Please Contact Your Bank.")
else:
  
  running = True
  while running == True:
    print("===================================")
    print("           ATM MAIN MENU           ")
    print("===================================")
    print("1. Balance Enquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Change PIN")
    print("5. Exit")
    print("===================================")

    choice = input("Enter Your Choice : ")

    
    if choice == "1":
      print("Available Balance : ₹", balance)

    
    elif choice == "2":
      amount = int(input("Enter Withdrawal Amount : ₹"))
      if amount <= 0:
        print("Amount must be greater than zero.")
      elif amount % 100 != 0:
        print("Amount must be a multiple of ₹100.")
      elif amount > 20000:
        print("Maximum withdrawal limit per transaction is ₹20,000.")
      elif amount > balance:
        print("Insufficient balance.")
      else:
        balance = balance - amount
        print("Please Collect Your Cash.")
        print("========== RECEIPT ==========")
        print("Transaction : Cash Withdrawal")
        print("Amount Withdrawn : ₹", amount)
        print("Available Balance : ₹", balance)
        print("=============================")

    
    elif choice == "3":
      deposit = int(input("Enter Deposit Amount : ₹"))
      if deposit <= 0:
        print("Deposit amount must be greater than zero.")
      else:
        balance = balance + deposit
        print("Deposit Successful.")
        print("Updated Available Balance : ₹", balance)

    
    elif choice == "4":
      current_pin = input("Enter current PIN : ")
      if current_pin == stored_pin:
        new_pin = input("Enter new 4-digit PIN : ")
        if len(new_pin) == 4 and new_pin.isdigit():
          confirm_pin = input("Confirm new 4-digit PIN : ")
          if new_pin == confirm_pin:
            stored_pin = new_pin
            print("PIN changed successfully.")
          else:
            print("New PIN entries do not match.")
        else:
          print("PIN must contain exactly four numeric digits.")
      else:
        print("Incorrect current PIN.")

    
    elif choice == "5":
      print("Thank you for using our ATM.")
      print("Available Balance : ₹", balance)
      running = False

    else:
      print("Invalid choice. Please select between 1 and 5.")
