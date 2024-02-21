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
