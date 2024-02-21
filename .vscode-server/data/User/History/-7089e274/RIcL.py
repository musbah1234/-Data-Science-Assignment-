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

