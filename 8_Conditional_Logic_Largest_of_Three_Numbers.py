"""
Largest of Three Numbers: Find the largest number among three user-provided numbers.
"""


try:
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    num3 = int(input("Please enter your third number: "))

    if (num1 > num2) and (num1 > num3):
        print("First number is the largest number.")
    elif (num2 > num1) and (num2 > num3):
        print("Second number is the largest number.")
    else:
        print("Third number is the largest number.")

except ValueError:
    print("Invalid input. Please enter a number.")