"""
many thanks to github.com/learnbyexample for these exercises
full exercises at https://github.com/learnbyexample/Python_Basics/blob/master/Exercises.md
"""

"""
Q1a) Ask user information, for ex: name, department, college etc
and display them using print function
"""

# # Sample of how program might ask user input and display output afterwards
# $ ./usr_ip.py
# Please provide the following details
# Enter your name: learnbyexample
# Enter your department: ECE
# Enter your college: PSG Tech

# ------------------------------------
# Name       : learnbyexample
# Department : ECE
# College    : PSG Tech


def userDetailsCollector():
    """prints out details the user inputs"""
    print("Please provide the following details")
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    college = input("Enter your college: ")
    print(f"Name       : {name}")
    print(f"College    : {college}")
    print(f"Department : {department}")


userDetailsCollector()
