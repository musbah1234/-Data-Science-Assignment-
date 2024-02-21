# Definition: map applies a given function to all items in an iterable and returns an iterable of the results.
# Definition: filter filters out elements from an iterable based on a given function.
# Definition: reduce cumulatively applies a binary function to the items in an iterable to reduce it to a single cumulative result.
# Definition: A higher-order function is a function that takes one or more functions as arguments or returns a function as its result
# Definition: A closure is a nested function that captures and remembers the values in the enclosing function's scope even if the outer function has finished execution.
# Definition: A decorator is a design pattern in Python that allows the modification or extension of functions or methods without changing their code.

countries = ["Armania", "Nigeria", "china"]
for country in countries:
    print(country)


names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# 1. Use map to create a new list by changing each country to uppercase in the countries list:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercased_countries = list(map(str.upper, countries))
print(uppercased_countries)

# 2. Use map to create a new list by changing each number to its square in the numbers list:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# 3. Use map to change each name to uppercase in the names list:
names = ['Alice', 'Bob', 'Charlie']
uppercased_names = list(map(str.upper, names))
print(uppercased_names)

#  Use filter to filter out countries containing 'land':

countries_with_land = list(filter(lambda country: 'land' not in country.lower(), countries))
print(countries_with_land)

# 5. Use filter to filter out countries having exactly six characters:

six_char_countries = list(filter(lambda country: len(country) != 6, countries))
print(six_char_countries)

# 6. Use filter to filter out countries containing six letters and more in the country list:
countries_six_letters_or_more = list(filter(lambda country: len(country) >= 6, countries))
print(countries_six_letters_or_more)

# 7. Use filter to filter out countries starting with an 'E':

countries_without_E = list(filter(lambda country: not country.startswith('E'), countries))
print(countries_without_E)

# 8. Chain two or more list iterators:
# Example chaining map, filter, and reduce
from functools import reduce

# Your existing code
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

# Declare a function called get_string_lists:

def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

# 10. Use reduce to sum all the numbers in the numbers list:

from functools import reduce
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

# 11. Use reduce to concatenate all the countries:

from functools import reduce
concatenated_countries = reduce(lambda x, y: f"{x}, {y}", countries)
print(concatenated_countries)

# 12. Declare a function called categorize_countries:

def categorize_countries(country_list):
    # Implement your logic here based on common patterns
    pass

# 13. Create a function returning a dictionary:

def country_starting_letters_count(country_list):
    starting_letters_count = {}
    for country in country_list:
        starting_letter = country[0].upper()
        starting_letters_count[starting_letter] = starting_letters_count.get(starting_letter, 0) + 1
    return starting_letters_count

# 14. Declare a get_first_ten_countries function:
def get_first_ten_countries():
    # Implement loading the list of countries and returning the first ten
    pass

# 15. Declare a get_last_ten_countries function:

def get_last_ten_countries():
    # Implement loading the list of countries and returning the last ten
    pass

