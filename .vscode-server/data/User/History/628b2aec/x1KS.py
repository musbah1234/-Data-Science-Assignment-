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
'''
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))
perimeter = a + b + c
print(f"The perimeter of a triangle is: {perimeter}")