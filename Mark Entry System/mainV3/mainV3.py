"""
This module serves as the main entry point for the CLI-based student marks management system.
It includes functions for displaying menus, handling user inputs, and managing student marks data.
The module leverages the 'fileOperation' module for loading and saving student marks to and from a file.

Functions:
- display_menu(): Displays the main menu options to the user.
- get_mark(): Prompts the user to enter a student's name and mark and stores this information.
- display_mark(): Displays all the stored student marks.
- CLI_menu(): The primary function that runs the Command Line Interface (CLI) menu loop, handling various user interactions.

The module demonstrates basic concepts of modular programming in Python, function definitions, loops, conditionals,
and file handling through external modules.

When run as the main program, it initializes the student marks list and starts the CLI menu loop to interact with the user.
"""


# Example Code V3
# By Firat


# Importing the fileOperation module
import fileOperation as FO

# -----------------------------
# Function Definitions
# -----------------------------

def draw_line(length=20, symbol="="):
    """
    Draws a line consisting of a repeated symbol.
    """
    line = length * symbol
    print(line)

def display_message(size=10, msg=""):
    """
    Displays a message within a frame of symbols.

    Parameters:
    size (int): The total width of the message display including the frame. Default is 10.
    msg (str): The message to be displayed. Default is an empty string.

    Returns:
    None: This function prints the message within a frame and returns nothing.
    """
    symbol = "*"
    size_msg = len(msg)
    side_size = int((size - size_msg) / 2)
    side_line = side_size * symbol
    draw_line(size)
    print(side_line + msg + side_line)
    draw_line(size)
    
def display_mark():
    """
    Displays all stored student marks.
    """
    for smark in studentMarks:
        print(smark)


def get_mark():
    """
    Prompts the user to enter a student's name and mark, then stores them.
    """
    sName = input("Please enter a student's name: ")
    sMark = input("Please enter the student's mark: ")
    studentMarks.append([sName, sMark])
    print(studentMarks)

# -----------------------------
# Menu Operations
# -----------------------------

def display_menu():
    """
    Displays the main menu options to the user, including options to manage student marks and file operations.
    """
    display_message(20, "Menu")
    print("h) say Hi")
    print("b) say Bye")
    print("m) get student mark")
    print("d) display marks")
    print("l) load the marks from a file")
    print("s) save the marks to a file")
    print("e) exit")

def CLI_menu():
    """
    Runs the Command Line Interface (CLI) menu loop,
    processing user input for various operations including file handling.
    """
    global studentMarks
    studentMarks = []
    
    while True:
        display_menu()
        option = input("Please enter your option: ")
        if option == "h":
            print("Hi")
        elif option == "m":
            get_mark()
        elif option == "d":
            display_mark()
        elif option == "b":
            print("Bye")
        elif option == "l":
            studentMarks = FO.load_marks()
        elif option == "s":
            FO.save_marks(studentMarks)
        elif option == "e":
            print("Bye bye, end of the program")
            break
        else:
            print("Wrong option")


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
  
    CLI_menu()

