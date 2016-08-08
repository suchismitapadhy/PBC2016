#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    If it encounters a non lower case letter in the 1st position, it will return false and will not check further
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    'c' is no longer a variable that we use to iterate over our string. It is a string constant and will always return True

    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    This function returns the last value of the flag, essentially checking if the last character of the string is lower or not.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    nothing is wrong
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    if c encounters a non lower case letter at the beginning it will return false and not check further
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    
    print(any_lowercase1("Thisstringmessesupthefunction"))
    


if __name__ == '__main__':
    main()
