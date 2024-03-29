# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [num for num in numbers if num <= 0]

print("Filtered Numbers:", filtered_numbers)


# Flatten the list of lists of lists to a one-dimensional list using Python

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]

print("Flattened List:", flattened_list)


# Using list comprehension to create the specified list of tuples in Python

result_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print("Resulting List of Tuples:")
print(result_list)


# Flatten the list of countries to a new list in the specified format using python

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Use list comprehension to create the flattened list
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for country in countries]

# Print the resulting list
print("Flattened List of Countries:")
print(flattened_countries)
