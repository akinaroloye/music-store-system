# Example Code V1
# Command Line Interface (CLI) Menu and List Operations
# By Firat 

# --------------------
# Function Definitions
# --------------------

def draw_line(length = 20 , symbol = "="):
    """
    Draws a line consisting of a repeated symbol.
    """
    line = length * symbol
    print(line)

def display_message(size = 10 , msg = ""):
    """
    Displays a message within a frame of symbols.
    """
    symbol = "*"
    size_msg = len(msg)
    side_size = int((size - size_msg) / 2)
    side_line = side_size * symbol
    draw_line(size)
    print(side_line + msg + side_line)
    draw_line(size)

def display_menu():
    """
    Displays the main menu options to the user.
    """
    display_message(20, "Menu")
    print("h) say Hi")
    print("b) say Bye")
    print("m) get student mark")
    print("d) display marks")
    print("s) stop")

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

def CLI_menu():
    """
    Runs the Command Line Interface (CLI) menu loop.
    """
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
        elif option == "s":
            print("Bye bye, end of the program")
            break
        else:
            print("Wrong option")

# -----------------------------
# Main Program
# -----------------------------
studentMarks = []
CLI_menu()
