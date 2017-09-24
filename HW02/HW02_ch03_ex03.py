#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_four(funcName,symbol):
	funcName(symbol)
	funcName(symbol)
	funcName(symbol)
	funcName(symbol)

def printSymbols(symbol):
	print(symbol,end=' ')	

def do_twice(funcName):
	funcName()
	funcName()

def RowContent():
	do_four(printSymbols,"-")
	print("+",end=' ')
	do_four(printSymbols,"-")
	print("+",end=' ')


def printRow2():
	print("+",end=' ')
	RowContent()
	print()

def printRow4():
	print("+",end=' ')
	do_twice(RowContent)
	print()
	
def bodyContent():
	do_four(printSymbols," ")
	print("|",end=' ')
	do_four(printSymbols," ")
	print("|",end=' ')

def printBody2(symbol):
	print("|",end=' ')
	bodyContent()
	print()

def printBody4(symbol):
	print("|",end=' ')
	do_twice(bodyContent)
	print()

def innerBlock(d):
	printBody(d)
	printBody(d)
	print()
	



def two_by_two():
	printRow2()
	do_four(printBody2,"")
	printRow2()
	do_four(printBody2,"")
	printRow2()
	
def four_by_four():
	printRow4()
	do_four(printBody4,"")
	printRow4()
	do_four(printBody4,"")
	printRow4()
	do_four(printBody4,"")
	printRow4()
	do_four(printBody4,"")
	printRow4()




# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()