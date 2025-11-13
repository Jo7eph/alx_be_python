# pattern_drawing.py
# This script draws a square pattern of asterisks (*) using nested loops.

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to new line
    print()  # Move to the next line after one row is complete
    row += 1  # Increment row counter
