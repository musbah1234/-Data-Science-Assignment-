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


numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercased_countries = list(map(str.upper, countries))
print(uppercased_countries)
