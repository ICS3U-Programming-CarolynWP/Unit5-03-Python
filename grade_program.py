# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/28
# Gets a level mark then uses a Switch Case
# Statement to determine the middle percentage.
# Uses a return value to get the percentage back to
# Main() where it is then displayed to the user.


# Function to calculate the marks
def calc_mark(mark):
    # "Switch Case" statement for the percentages
    marks = {
        "4+": 97.5,
        "4": 90.5,
        "4-": 83,
        "3+": 78,
        "3": 74.5,
        "3-": 71,
        "2+": 68,
        "2": 64.5,
        "2-": 61,
        "1+": 58,
        "1": 54.5,
        "1-": 51,
        "R": "-50",
    }
    # To return the values. If the input is different, return
    # -1
    return marks.get(mark, "-1")


# Getting the user input and return value, and
# Displaying the output
def main():
    # Title of the program
    print("The Grade Program!")

    # User input
    user_mark = input("Please enter a level mark: ")

    # Return value for the middle percentage
    percentage = calc_mark(user_mark)

    # If the return value is -1, this means there is an error
    if percentage == "-1":
        print("Please enter a valid level!")
    else:
        print("The middle percentage mark is {}%!".format(percentage))


if __name__ == "__main__":
    main()
