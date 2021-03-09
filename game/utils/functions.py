import random
import sys

def beginning_prompt():
    print(
        "Hello player! This is Rock Paper Scissors. For rock type R, Paper P and Scissors S."
        " To leave the program. Type x. This is not case sensitive")


def incorrect_input():
    print("This input is incorrect. Please type R for Rock, P for Paper, S for Scissors, or X to Leave")


def leave_program_prompt():
    print("Thank you for playing")


def get_rps():
    num = random.randint(1, 3)
    if num == 1:
        return "R"
    elif num == 2:
        return "P"
    else:
        return "S"


def shape_input(val):
    while(True):
        new_val = val.upper()
        if new_val == 'X':
            sys.exit()
        if new_val == 'R':
            return 'R'
        elif new_val == 'P':
            return 'P'

        elif new_val == 'S':
            return 'S'
        else:
            val = input("Please type R for Rock, S for Scissors, P for Paper of X to leave")



def check_if_winner(user_input, comp_input):
    if user_input == 'R':
        if comp_input == 'R':
            print ("Tied. Rock and Rock")
            return 0
        elif comp_input == 'P':
            print ("You lost. You had Rock and they had Paper")
            return -1
        else:
            print ("You won. You had Rock and they had Scissors")
            return 1
    elif user_input == 'P':
        if comp_input == 'R':
            print ("You won. You had Paper and they had Rock")
            return 1
        elif comp_input == 'P':
            print ("Tied. Paper and Paper")
            return 0
        else:
            print ("You lost. You had Paper and they had Scissors")
            return -1
    else:
        if comp_input == 'R':
            print ("You lost. You had Scissors and they had Rock")
            return -1
        elif comp_input == 'P':
            print ("You won. You had Scissors and they had Paper")
            return 1
        else:
            print ("Tied. Scissors and Scissors")
            return 0


def print_check_if_play_again():
    print ("Do you want to play again. Y for yes or N for No")


def check_if_play_again():
    while (True):
        val = input("Input: ")
        new_val = val.upper()
        if new_val == 'Y':
            print ("Playing again")
        elif new_val == 'N':
            print ("Thanks for playing")
            sys.exit()
        else:
             print("Please type Y for Yes, N for No: ")


def tally_score(wins, loses, ties):
    print ("You have %s wins, %s loses and %s ties" % (wins, loses, ties))