
"""
fileOperation Module

This module contains functions for handling file operations related
to the student marks management system.
It includes functionalities to load student marks from
a file and save current marks to a file. 

Functions:
- load_marks(): Reads student marks from a 'StudentMarks.txt' file
and returns a list of these marks.
Each mark is a list containing the student's name and their mark.
Handles file not found and other exceptions, returning an empty list or
the current state of the list in such cases.
- save_marks(studentMarks): Accepts a list of student marks and
writes them to the 'StudentMarks.txt' file.
Handles exceptions related to file writing operations.

This module simplifies file operations for the main application,
encapsulating complex functionalities and providing easy-to-use interfaces
for reading and writing student data.
"""

# update Date : ...
# Version 0.1
# by : Firat

# -----------------------------
# Function Definitions
# -----------------------------

def load_marks():
    """
    Loads student marks from a file and returns the list of marks.

    Parameters:
    None

    Returns:
    list: A list containing the loaded student marks.
    Each mark is a sublist containing the student's name and mark.
    """
    studentMarks = []  # Initialize an empty list to store student marks
    try:
        with open("StudentMarks.txt", "r") as f:
            for markinfo in f:
                clean_markinfo = markinfo.strip()
                studentMark = clean_markinfo.split(",")
                studentMarks.append(studentMark)
        print("All the marks have been loaded into the memory successfully")
        return studentMarks  # Return the populated list of student marks
    except FileNotFoundError:
        print("Error: The file 'StudentMarks.txt' was not found.")
        return studentMarks  # Return the empty list if the file is not found
    except Exception as e:
        print(f"An error occurred: {e}")
        return studentMarks  # Return the list as is in case of other exceptions


def save_marks(studentMarks):
    """
    Saves the current student marks to a file.

    Parameters:
    studentMarks (list): The list of student marks to be saved.

    Returns:
    None: This function writes the current marks in studentMarks list to a file.
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
# Main Program
# -----------------------------

if __name__ == "__main__":
    
    # Test cases or demonstration for the functions in fileOperation module

    # Demonstrating load_marks function
    print("Testing load_marks function:")
    marks_loaded = load_marks()
    print(f"Loaded marks: {marks_loaded}")

    # Assuming marks_loaded is not empty, we can test save_marks function
    if marks_loaded:
        print("\nTesting save_marks function with the loaded marks:")
        save_marks(marks_loaded)
        print("Marks have been saved successfully.")
    else:
        print("\nNo marks loaded, skipping save_marks test.")
