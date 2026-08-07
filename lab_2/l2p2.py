# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:18:43 2026

@author: maths
"""

def getMarks():
    name = input("Enter Student Name : ")
    usn = input("Enter USN : ")
    print("Enter Marks of Five Subjects")
    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))
    m4 = int(input("Subject 4: "))
    m5 = int(input("Subject 5: "))
    return name, usn, [m1, m2, m3, m4, m5]

def calculateTotal(marks):
    return sum(marks)

def calculatePercentage(total):
    return (total / 500) * 100

def calculateGrade(percentage, marks):
    if any(m < 50 for m in marks):
        return 'F', 'FAIL'
    if percentage >= 90:
        return 'A+', 'PASS'
    elif percentage >= 80:
        return 'A', 'PASS'
    elif percentage >= 70:
        return 'B', 'PASS'
    elif percentage >= 60:
        return 'C', 'PASS'
    elif percentage >= 50:
        return 'D', 'PASS'
    else:
        return 'F', 'FAIL'

def displayResult(name, usn, marks, total, percentage, grade, result):
    print("\nSTUDENT RESULT PROCESSING")
    print(f"Enter Student Name : {name}")
    print(f"Enter USN : {usn}")
    print("Enter Marks of Five Subjects")
    for i in range(5):
        print(f"Subject {i+1}: {marks[i]}")
    print("\nSTUDENT RESULT")
    print(f"Student Name : {name}")
    print(f"USN : {usn}")
    for i in range(5):
        print(f"Subject {i+1} Marks : {marks[i]}")
    print(f"Total Marks : {total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade : {grade}")
    print(f"Result : {result}")

name, usn, marks = getMarks()
total = calculateTotal(marks)
percentage = calculatePercentage(total)
grade, result = calculateGrade(percentage, marks)
displayResult(name, usn, marks, total, percentage, grade, result)
