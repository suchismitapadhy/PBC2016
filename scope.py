#!/usr/bin/env python
# HW02_ch03_ex01

# Yesterday we struggled with figuring out scope in and out of functions.

# Example 1
x = 10


def ex1():
    print(x, "{}".format("ex1"))


# Example 2
def ex2():
    if False:
        x = 1
    print(x, "{}".format("ex2"))


def main():
    """Call your functions within this function."""
    ex1()
    ex2()

if __name__ == "__main__":
    main()
