#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


# Body
def count(word,letter):
	# word = 'banana'
    count_letters = 0
    for l in word:
        if l == letter:
            count_letters = count_letters + 1
    print(count_letters)



###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    word=input("Enter a word: ")
    letter=input("Enter the letter you want to count: ")
    count(word,letter)



if __name__ == '__main__':
    main()
