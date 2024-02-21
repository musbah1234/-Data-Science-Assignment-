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
add_all_nums(1, 2, 3) 
add_all_nums(1, 'a', 3) 

# Temperature in °C can be converted to °F using this formula: 
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temperature = 25.0
fahrenheit_result = convert_celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is equal to {fahrenheit_result}°F")

# Write a function called check-season, 
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer

def check_season(month):
    
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

month_input = 7
result_season = check_season(month_input)
print(f"The season for month {month_input} is {result_season}")


# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
     
    # Ensure the denominator is not zero to avoid division by zero
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
        return slope
    else:
        # Handle the case when x2 - x1 is zero
        raise ValueError("The denominator (x2 - x1) cannot be zero.")

x1, y1 = 1, 2
x2, y2 = 3, 4
result_slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the linear equation is: {result_slope}")

# Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn. using python

import cmath  # Importing cmath for handling complex roots

def solve_quadratic_eqn(a, b, c):
   
    # Calculate the discriminant
    delta = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two solutions using the quadratic formula
    root1 = (-b + delta) / (2*a)
    root2 = (-b - delta) / (2*a)

    return root1, root2

a, b, c = 1, -3, 2
result_roots = solve_quadratic_eqn(a, b, c)
print(f"The roots of the quadratic equation are: {result_roots}")

# Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.

def print_list(my_list):
   
    for item in my_list:
        print(item)

my_list_example = [1, 2, 3, 4, 5]
print_list(my_list_example)

# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(input_array):
  
    reversed_array = []
    for i in range(len(input_array) - 1, -1, -1):
        reversed_array.append(input_array[i])
    return reversed_array


my_array_example = [1, 2, 3, 4, 5]
result = reverse_list(my_array_example)
print(result)



# Declare a function named capitalize_list_items. 
# it takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(input_list):
   
    return [item.capitalize() for item in input_list]


my_list_example = ["apple", "banana", "cherry"]
result = capitalize_list_items(my_list_example)
print(result)


# Declare a function named add_item. 
# It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list, new_item):
   
    return input_list + [new_item]


# Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.

def remove_item(input_list, item_to_remove):
    
    new_list = input_list.copy()  # Create a copy to avoid modifying the original list
    try:
        new_list.remove(item_to_remove)
    except ValueError:
        print(f"{item_to_remove} not found in the list.")
    return new_list

my_list = [1, 2, 3, 4, 5]
result = remove_item(my_list, 3)
print(result)


my_list = [1, 2, 3]
result = add_item(my_list, 4)
print(result)

# Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(end_number):
    
    return sum(range(1, end_number + 1))

result = sum_of_numbers(5)
print(result)  # Output: 15

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(end_number):
    \
    return sum(i for i in range(1, end_number + 1) if i % 2 != 0)


result = sum_of_odds(10)
print(result)  # Output: 25

# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(end_number):
   
    return sum(i for i in range(1, end_number + 1) if i % 2 == 0)

result = sum_of_even(10)
print(result)  










