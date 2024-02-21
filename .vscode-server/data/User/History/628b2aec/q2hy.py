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
'''  
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius =  int(input("Enter radius"))
cir_area = 3.14 * ( radius**2 )
cir_circumference = 2 * 3.14 * (radius)
print (f" the area of a circle is: {cir_area} \nAnd the circumference of a circle is: {cir_circumference}")