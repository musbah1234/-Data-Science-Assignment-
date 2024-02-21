# declare a function add_two_numbers. It takes two parameters and it returns a sum.

def adding():
    print( 1 + 2 )
    
adding()

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math

def area_of_circle(radius):
    
    area = math.pi * radius * radius
    return area

radius = 5.0
result = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {result}")

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    
    # Check if all items are of number type
    if all(isinstance(arg, (int, float)) for arg in args):
        result = sum(args)
        print(f"Sum of the numbers: {result}")
        return result
    else:
        print("Error: Not all items are of number type.")
        return None

# Example usage:
add_all_nums(1, 2, 3)  # Output: Sum of the numbers: 6
add_all_nums(1, 'a', 3)  # Output: Error: Not all items are of number type.

