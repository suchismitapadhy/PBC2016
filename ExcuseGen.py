#!/usr/bin/env python3
# Imports
import random


# Body
def printRoster(roster):
    """ prints entire roster """
    for x in roster:
        print(x)


def getRandomParticipantIndex(roster):
    """ Returns random index of person in roster """
    return random.randint(0, len(roster) - 1)


def getPerson(roster,index):
    """ Returns person (string) from roster """
    # rewrite getPerson() to take a index and roster; return name at index
    return roster[index]


def addPerson(roster,name):
    """ Adds person (string) to roster """
    # rewrite addStudent() to take a name and roster; add name to roster
    roster.append(name)


def get_excuse():
    excuses = ["My dog ate my homework",
               "I drank too much beer last night.",
               "\"Bored to Death\" marathon",
               "Laptop went up in flames",
               "Ain't nobody got time for that!",
               "My plane got stuck in Vegas",
               "I was watching \"The Big Lebowski\"",
               "Wait, I was supposed to do something?"]

    return excuses[random.randint(0, len(excuses) - 1)]


###############################################################################
def main():
    """ Main -- prints the bootcamp roster, adds Daniel, and then prints
    excuses """
    bootcampParticipants = ["Malavika", "Edward", "Nancy", "Ankeet", "Anna",
                            "Arnav", "Sandeep", "Shannon", "Natalia", "Nia",
                            "Nicolas", "Nihar", "Suchismita", "Vikram", "Yifei",
                            "Avi", "Nisha", "Peter", "Priyanka", "Rohit",
                            "Sophie", "Selenne", "Carina", "Lucia", "Meghana",
                            "Harman", "Robin", "Karan", "Liz", "Shazeda",
                            "Jolly", "Michelle", "Morgan", "Mudit"]

    # your one line of code goes here to print roster #
    printRoster(bootcampParticipants)

    # add 'Daniel' to bootcampParticipants
    addPerson(bootcampParticipants,"Daniel")

    # Your Code Here ###
    # get random participant 
    name=getPerson(bootcampParticipants,getRandomParticipantIndex(bootcampParticipants))

    
    # print person's name who has excuse today.
    # Fix code below to print name and excuse of person:
    print("{} said: {}".format(name, get_excuse()))


if __name__ == "__main__":
    print("Excuse Generator: ") 
    main()
