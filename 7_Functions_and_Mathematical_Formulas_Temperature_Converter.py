"""
Temperature Converter: Convert a temperature from Celsius to Fahrenheit and vice versa.
Fahrenheit = (Celsius * 9/5) + 32
Celsius = (Fahrenheit - 32) * 5/9
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    print("1. Convert celsius to fahrenheit.")
    print("2. Convert fahrenheit to celsius.")

    try:
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            celsius = float(input("Enter temperature in celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter only numbers for the temperature.")


# ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()

