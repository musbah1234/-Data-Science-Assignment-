# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [num for num in numbers if num <= 0]

print("Filtered Numbers:", filtered_numbers)
