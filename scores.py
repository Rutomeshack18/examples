#!/bin/bash
score=int(input("Enter your score: "))
if score>= 90:
    grade= "A"
elif score>= 80:
    grade= "B+"
elif score>= 70:
    grade= "B"
elif score>=60:
    grade= "B-"
else:
    grade= "C"
print("Your grade is", grade)
