# multiplication_table.py
# This script generates a multiplication table for a given number using a for loop.

# Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and display the multiplication table from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
