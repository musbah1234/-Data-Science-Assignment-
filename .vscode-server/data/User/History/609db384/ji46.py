from collections import Counter
import re

# Given paragraph
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Tokenize the paragraph into words
words = re.findall(r'\b\w+\b', paragraph.lower())

# Count the frequency of each word
word_counts = Counter(words)

# Find the most frequent word
most_frequent_word = word_counts.most_common(1)[0][0]

# Print the result
print("The most frequent word is:", most_frequent_word)


# Given text containing particle positions
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers from the text
import re
numbers = [int(match) for match in re.findall(r'-?\d+', text)]

# Sort the numbers
sorted_points = sorted(numbers)

# Find the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

# Print the result
print("Extracted Numbers:", sorted_points)
print("Distance between the two furthest particles:", distance)


Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
