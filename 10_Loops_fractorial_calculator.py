"""
Factorial Calculator: Calculate the factorial of a number using a loop.
"""
num = int(input("Enter a number: "))
factorial_result = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial_result = factorial_result * i

    print(f"Factorial of {num} is {factorial_result}.")