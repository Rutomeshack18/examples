#!/bin/bash
#Guessing game for a random number
secret_number= int(input("Enter the secret number between 1 and 10: "))
while secret_number < 1 or secret_number > 10:
	secret_number = int(input("Invalid number. Enter only a number between 1 and 10: "))
guess=0
guess_count=0
while guess != secret_number:
	guess= int(input("Enter your guess: "))
	guess_count += 1
	if guess != secret_number:
 		print("Guess again kiddo")
print("You guessed correct in", guess_count,"times !!Hoooray")
