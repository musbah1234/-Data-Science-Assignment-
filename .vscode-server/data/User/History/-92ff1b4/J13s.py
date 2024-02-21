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

python_for_all = company
modified = python_for_all.replace('coding', 'python')
print(modified)

# Change Python for Everyone to Python for All using the replace method or other methods.

pro_modified = modified.replace('python For All', 'python for everyone')
print(pro_modified)

# Split the string 'Coding For All' using space as the separator (split())

split_result = pro_modified.split()

print(split_result)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

FGMAIOA = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

FGMAIOA_Result = FGMAIOA.split()

print(FGMAIOA_Result)

# What is the character at index 0 in the string Coding For All.

index_at_o = pro_modified[0]

print(index_at_o)

# What is the last index of the string Coding For All.

index_last = pro_modified[-1]

print(index_last)

# What character is at index 10 in "Coding For All" string.

index_10 = pro_modified[10]

print(index_10)

# Create an acronym or an abbreviation for the name 'Python For Everyone'

acrm = pro_modified.split()

acronym = ''.join([acr[0].upper() for acr in acrm])

print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.

acrm2 = company.split()

acronym2 =  ''.join([acr2[0].upper() for acr2 in acrm2])

print(acronym2)

# Use index to determine the position of the first occurrence of C in Coding For All.

position = company.index('c')

print(f"The position of the first occurrence of 'c' is: {position}")

# Use index to determine the position of the first occurrence of F in Coding For All.

position_F = company.index('F')

print(f"The position of the first occurrence of 'F' is: {position_F}")

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

position_l = company.rfind('l')

print(f"The position of the first occurrence of 'l' is: {position_l}")

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

sent_Be = 'You cannot end a sentence with because because because is a conjunction'

split_sent = sent_Be.split()

position_Sent = split_sent.index('because')

print(f"The position of the first occurrence of 'because' is: {position_Sent}")

# Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction

sentence = 'You cannot end a sentence with because because because is a conjunction'

# Using rindex to find the position of the last occurrence of 'because'
position_last_because = sentence.rindex('because')

# Printing the result
print(f"The position of the last occurrence of 'because' is: {position_last_because}")

# Slice out the phrase 'because because because' in the following sentence:
#'You cannot end a sentence with because because because is a conjunction'

# Given sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'

# Slicing to get the desired phrase
desired_phrase = sentence[sentence.find('because'): sentence.rfind('because') + len('because')]

# Printing the result
print(f"The sliced phrase is: '{desired_phrase}'")

# Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'

# Given sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'

# Finding the position of the first occurrence of 'because'
position_of_because = sentence.find('because')

# Printing the result
print(f"The position of the first occurrence of 'because' is: {position_of_because}")



