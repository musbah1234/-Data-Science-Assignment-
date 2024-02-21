'''
age = 30
height = 1.7
complex_num = 2 + 2j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter base:"))
Height = float(input("Enter height:"))
area = 0.5 * ( base * Height )
area_as_integer = int(area)
print (f"The area of a triangle is: {area_as_integer}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))
perimeter = a + b + c
print(f"The perimeter of a triangle is: {perimeter}")

# Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
rec_area = length * width
rec_perimeter = 2 * (length + width)
print (f"The area of a rectangle is: {rec_area} \nAnd the perimeter of a rectangle is: {rec_perimeter}")
 
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius =  int(input("Enter radius"))
cir_area = 3.14 * ( radius**2 )
cir_circumference = 2 * 3.14 * (radius)
print (f"The area of a circle is: {cir_area} \nAnd the circumference of a circle is: {cir_circumference}")


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Equation: y = 2x - 2

slope = 2

x_intercept = 2 / slope

y_intercept = -2

print(f"Slope (m): {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

# Coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope (m)
slope = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Slope (m): {slope}")
print(f"Euclidean Distance: {distance}")

'''
# Compare the slopes in tasks 8 and 9.

import math

# Coordinates of the points for Task 8
x1_task8, y1_task8 = 2, 2
x2_task8, y2_task8 = 6, 10

# Slope calculation for Task 8
slope_task8 = (y2_task8 - y1_task8) / (x2_task8 - x1_task8)

# Coordinates of the points for Task 9
x1_task9, y1_task9 = 1, 3
x2_task9, y2_task9 = 5, 7

# Slope calculation for Task 9
slope_task9 = (y2_task9 - y1_task9) / (x2_task9 - x1_task9)

# Comparing slopes
if slope_task8 > slope_task9:
    comparison_result = "The slope in Task 8 is greater than the slope in Task 9."
elif slope_task8 < slope_task9:
    comparison_result = "The slope in Task 8 is less than the slope in Task 9."
else:
    comparison_result = "The slopes in Task 8 and Task 9 are equal."

# Printing the results
print(f"Slope in Task 8: {slope_task8}")
print(f"Slope in Task 9: {slope_task9}")
print(comparison_result)




