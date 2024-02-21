'''
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a = "Thirty"
b = "Days"
c = "Of"
d = "Python"

print(a + " " + b + " " + c + " " + d)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

a = 'Coding'
b = 'For'
c = 'All'

print (a+" "+b+" "+c)

# Declare a variable named company and assign it to an initial value "Coding For All".
'''
company = ("coding For All")

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print()

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company.split()[0])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

try:
    index_result = company.index('coding')
    print(f"'Coding' found at index {index_result}")
except ValueError:
    print("'Coding' not found using index()")

# Replace the word coding in the string 'Coding For All' to Python.  

 
print(company.replace('coding', 'python'))  

# Change Python for Everyone to Python for All using the replace method or other methods.

modified = python_for_all.replace('python For All', 'python for everyone')
print(modified)




