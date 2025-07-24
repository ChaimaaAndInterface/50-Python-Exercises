"""
Simple Calculator: Create a program that takes two numbers as input and performs
addition, subtraction, multiplication, and division.
"""
try:
    first_number = int(input("Please enter your first number: "))
    second_number = int(input("Please enter your second number: "))

    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number

    print(f"Addition: {addition}" )
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")

    # Check for division by zero before performing the operation
    if second_number != 0:
        division = first_number / second_number
        print(f"Division: {division}")
    else:
        print("Division: Cannot division by zero.")

except ValueError:
    print("Invalid input. Please enter only number.")

