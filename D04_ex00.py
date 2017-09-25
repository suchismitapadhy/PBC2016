#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports


# Body
import random
def guess():
	number=random.randint(1,25)
	for i in range(5):
		try:
			my_number=int(input("Enter a number:"))
			if my_number==number:
				print("your guess was right")
				return
			elif my_number<number:
				print("your number is low")
				
			else:
				print("your number is high")
		except:
			print("Nice try. please enter a valid number")

				




################################################################################
def main():


    guess() # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()