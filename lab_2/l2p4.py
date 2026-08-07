# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:52:21 2026

@author: maths
"""

def registerPatient(name, age, gender, bloodGroup="Unknown", insurance="No"):
    print("\nPATIENT INFORMATION")
    print(f"Patient Name : {name}")
    print(f"Age          : {age}")
    print(f"Gender       : {gender}")
    print(f"Blood Group  : {bloodGroup}")
    print(f"Insurance    : {insurance}")

p_name = input("Enter Patient Name : ")
p_age = input("Enter Age : ")
p_gender = input("Enter Gender (M/F): ")

bg_input = input("Enter Blood Group (Press Enter to Skip): ")
ins_input = input("Enter Insurance (Yes/No) (Press Enter to Skip): ")

kwargs = {}
if bg_input:
    kwargs["bloodGroup"] = bg_input
if ins_input:
    kwargs["insurance"] = ins_input

registerPatient(p_name, p_age, p_gender, **kwargs)
