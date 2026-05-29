# Example Code V2
# CLI Menu, List Operations, and File Handling
# By Firat

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
# File Operation Functions
# -----------------------------
def load_marks():
    """
    Loads student marks from a file into the program.
    """
    try:
        # Attempt to open the file in read mode
        with open("StudentMarks.txt", "r") as f:
            for markinfo in f:
                clean_markinfo = markinfo.strip()
                studentMark = clean_markinfo.split(",")
                studentMarks.append(studentMark)
        print("All the marks have been loaded into the memory successfully")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Error: The file 'StudentMarks.txt' was not found.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
    finally:
        # Always display the marks, even if there were errors
        display_mark()

def save_marks():
    """
    Saves the current student marks to a file.
    """
    try:

        with open("StudentMarks.txt", "w") as f:
            for mark in studentMarks:
                newRecord = mark[0] + "," + mark[1] + "\n"
                f.write(newRecord)
        print("All the marks have been saved into the disk successfully")
    except IOError:
        print("Error: Failed to write to 'StudentMarks.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
            load_marks()
        elif option == "s":
            save_marks()
        elif option == "e":
            print("Bye bye, end of the program")
            break
        else:
            print("Wrong option")


# -----------------------------
# Main Program
# -----------------------------
studentMarks = []
CLI_menu()
