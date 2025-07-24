"""
Even or Odd: Check if a given number is even or odd.
"""
try:
    number = int(input("Please enter a number: "))

    if number % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
except ValueError:
    print("Invalid value. Please enter only numbers.")