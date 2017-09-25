#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        num=int(input("Enter a valid number"))
        if num%2==0:
            print("Number is Even")
            
        else:
            print("Number is odd")
    except:
        print("number is not valid, try again")
    return





def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    num=1
    for i in range(10):
        for j in range(10):
            print(num,end=' ')
            num+=1
        print()
    


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    total=0
    n=0
    while True:
        number=input("Enter a number: ")
        if number=="done":
            if n==0:
                return 0
            return total/n
        try:
            total+=int(number)
            n+=1

        except:
            print("Enter a non-word numeral")




##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())
    

if __name__ == '__main__':
    main()
