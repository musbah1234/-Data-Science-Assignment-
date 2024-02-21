import os
import json
from collections import Counter

# Function to count lines and words in a text file
def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        words = ' '.join(lines).split()
        num_words = len(words)
    return num_lines, num_words

# Function to find the ten most spoken languages
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    languages = Counter()
    for country in data:
        if 'languages' in country:
            languages.update(country['languages'])

    return languages.most_common(top_n)

# Function to find the ten most populated countries
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

# Function to extract incoming email addresses from a file
def extract_email_addresses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        # Use a simple regex pattern to extract email addresses
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return email_addresses

# Function to find the most common words in English
def find_most_common_words(text, top_n):
    # Implementation of this function depends on the source of English words data
    # You may need to use pre-existing datasets or libraries for English words

# Function to check similarity between two texts
def check_text_similarity(text1, text2):
    # Implementation of this function depends on the chosen method for text similarity
    # It may involve cleaning the text, removing stop words, and using a similarity metric

# Function to find the ten most repeated words in a text file
def most_repeated_words(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(top_n)

# Function to count lines based on conditions in a CSV file
def count_lines_in_csv(filename, keyword1, keyword2, exclude_keyword):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    count_python = sum(keyword1.lower() in line.lower() or keyword2.lower() in line.lower() for line in lines)
    count_javascript = sum('javascript' in line.lower() for line in lines)
    count_java_not_javascript = sum('java' in line.lower() and 'javascript' not in line.lower() for line in lines)

    return count_python, count_javascript, count_java_not_javascript

# Example usages

# a) Count lines and words in Obama's speech
obama_lines, obama_words = count_lines_and_words('./data/obama_speech.txt')
print(f"Obama's speech: Lines - {obama_lines}, Words - {obama_words}")

# b) Count lines and words in Michelle Obama's speech
michelle_lines, michelle_words = count_lines_and_words('./data/michelle_obama_speech.txt')
print(f"Michelle Obama's speech: Lines - {michelle_lines}, Words - {michelle_words}")

# c) Count lines and words in Donald Trump's speech
donald_lines, donald_words = count_lines_and_words('./data/donald_speech.txt')
print(f"Donald Trump's speech: Lines - {donald_lines}, Words - {donald_words}")

# d) Count lines and words in Melina Trump's speech
melina_lines, melina_words = count_lines_and_words('./data/melina_trump_speech.txt')
print(f"Melina Trump's speech: Lines - {melina_lines}, Words - {melina_words}")

# Read countries_data.json and find the ten most spoken languages
languages_result = most_spoken_languages(filename='./data/countries_data.json', top_n=10)
print("Most Spoken Languages:")
print(languages_result)

# Read countries_data.json and find the ten most populated countries
populated_countries_result = most_populated_countries(filename='./data/countries_data.json', top_n=10)
print("Most Populated Countries:")
print(populated_countries_result)

# Extract email addresses from email_exchange_big.txt
email_addresses_result = extract_email_addresses('./data/email_exchange_big.txt')
print("Extracted Email Addresses:")
print(email_addresses
