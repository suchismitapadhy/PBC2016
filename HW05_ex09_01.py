#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

def read_file():
	with open('words.txt') as f:
		l=f.readlines()
		for word in l:
			if len(word)>20:
				print(word.strip('\n'))


##############################################################################
def main():
	read_file()      # Call your functions here.

if __name__ == '__main__':
    main()
