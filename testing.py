import random
import time


def displayIntro():
    print("Welcome to my adventure game!")
    time.sleep(2)
    print("You have come upon two doors.")
    print("One is marked with a large number 1.")
    print("The other is marked with a faded blue number 2.")
    time.sleep(2)
    print()


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Will you pick door 1 or door 2?")
    return path


def checkPath(choosePath):
    print("You walk towards the door.")
    time.sleep(2)
    print("Cautiously, you turn the handle and step inside... ")
    time.sleep(3)
    correctPath = str(random.randint(1, 2))


    if choosePath == correctPath:
        print("Inside you spot a warm fire, and a fluffy kitten")
        time.sleep(2)
        print("On the table, there is a plate of warm chocolate chip cookies.")
        time.sleep(2)
        print("You eat the deliciously warm chocolate chip cookies,")
        print("and snuggle by the fire with your new friend, Patrick the cat!")
        time.sleep(2)
        print("You have made an excellent choice! Congratulations!")
    else:
        print("You have opened the wrong door!")
        time.sleep(2)
        print("You have been slayed by a very angry old woman")
        print("weilding a cast iron frying pan and an unmeasureable rage")
        time.sleep(2)
        print("You are now D-E-D")


def game_over():
    print("Do you want to play again? Yes or No?")

    choice = ""
    while choice != "yes" and choice != "no":
        choice = input("> ").title()
        if choice == "Yes":
            game()
        elif choice == "No":
            exit(0)


def game():
    displayIntro()
    path = choosePath()
    checkPath(path)
    game_over()


game()
