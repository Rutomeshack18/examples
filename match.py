i#!/bin/bash
#Learning Match case in python
day = input("Enter any day of the week: ").lower()
match day:
case "monday":
	print("Ugh monday blues")
case "tuesday":
	print("Just another regular day")
case "wednesday":
	print("closer to the weekend")
case "thursday":
	print("Much closer Muhitos")
case "friday":
	print("Ni furahi day")
case "sartuday"|"sunday":
	print("Gotha tena")
case _:
	print("Not a correct day")
