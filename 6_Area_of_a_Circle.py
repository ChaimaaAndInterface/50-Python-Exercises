"""
Area of a Circle: Calculate the area of a circle given its radius. Area = πr².
"""
import math
try:
    radius = int(input("Please enter radius: "))
    area = math.pi * radius ** 2
    print(area)
except ValueError:
    print("Invalid value. Please enter only numbers.")