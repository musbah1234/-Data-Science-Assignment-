# Declare an empty list
empty_list = []


# Declare a list with more than 5 items

new_list = ['mango', 'Banana', 'Cashew', 'Orange', 'strawberry']

# Find the length of your list

list_len = len(new_list)

print(list_len)

# Get the first item, the middle item and the last item of the list


# Get the first item
first_item = new_list[0]

# Get the middle item
middle_item = new_list[len(new_list)//2]

# Get the last item
last_item = new_list[-1]

print("First Item:", first_item)
print("Middle Item:", middle_item)
print("Last Item:", last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["name", "age", "height", "marital status", "address"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()

print(_companies)

# Print the number of companies in the list

num_Of_Com = len(_companies)
print(num_Of_Com)

# Print the first, middle and last company

first_com = _companies[0]
second_Com  = _companies[len(_companies)//2]
last_com = _companies[-1]

print(first_com )
print( second_Com)
print(last_com) 

# Print the list after modifying one of the companies

modified_company_index = _companies.index("Google")
_companies[modified_company_index] = "Samsung"

# Print the modified list of companies
print("Modified List of Companies:", _companies)

# Add an IT company to it_companies

new_company = "IT company"

_companies.append(new_company)

print(_companies)

# Insert an IT company in the middle of the companies list

new_company2 = "IT company2"

mid_index = len(_companies)//2

_companies.insert(mid_index, new_company2)

print(_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

company_to_change = "Microsoft"

# Check if the selected company is not IBM
if company_to_change.upper() != "IBM":
    # Find the index of the selected company
    index_to_change = _companies.index(company_to_change)
    
    # Change the company name to uppercase
    _companies[index_to_change] = company_to_change.upper()

# Print the updated list
print("Updated IT Companies List:", _companies)

# Join the it_companies with a string '#;  '

joined_companies = '#; '.join(_companies)

# Print the result
print(joined_companies)

# Check if a certain company exists in the it_companies list.

com_to_check = "Microsoft"

if com_to_check in _companies:
    print(f"{com_to_check} exists in the list.")
else:
    print(f"{com_to_check} does not exists in the list.")

# Sort the list using sort() method

_companies.sort()

print(_companies)

# Reverse the list in descending order using reverse() method

_companies.sort(reverse=True)

print(_companies)

# Slice out the first 3 companies from the list

first3_com = _companies[:3]

print("First three companies:", first3_com)