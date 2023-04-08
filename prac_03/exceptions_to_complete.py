"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # set is_finished to True to exit the loop if an integer is successfully entered
    except ValueError:  # catch the ValueError exception that is raised when a non-integer is entered
        print("Please enter a valid integer.")
print("Valid result is:", result)
