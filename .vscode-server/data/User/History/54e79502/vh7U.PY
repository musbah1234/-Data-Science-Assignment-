# Change the function definition to accept a file path as a parameter
def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Obama speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/obama_speech.txt'

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")


#b
def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Michelle Obama speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/michelle_obama_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")

#c

def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Donald Trump speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/donald_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")



def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Melania Trump speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/melina_trump_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")




import json

def get_most_spoken_languages(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Extract languages and their speakers from the data
    languages_speakers = {}
    for country in countries_data:
        # Check if 'languages' is a dictionary before using items()
        if isinstance(country.get('languages', {}), dict):
            for language, speakers in country['languages'].items():
                if language in languages_speakers:
                    languages_speakers[language] += speakers
                else:
                    languages_speakers[language] = speakers

    # Sort languages by the number of speakers in descending order
    sorted_languages = sorted(languages_speakers.items(), key=lambda x: x[1], reverse=True)

    # Get the top ten languages
    top_ten_languages = sorted_languages[:10]

    return top_ten_languages

# Specify the file path for the countries_data.json file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/countries_data.json'  # Replace with the actual path to your file

# Call the function and get the results
most_spoken_languages = get_most_spoken_languages(file_path)

# Print the results
print("Ten Most Spoken Languages:")
for language, speakers in most_spoken_languages:
    print(f"{language}: {speakers} speakers")


import json

def get_ten_most_populated_countries(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Extract country and population information
    country_population = [(country['name'], country['population']) for country in countries_data]

    # Sort countries based on population in descending order
    sorted_countries = sorted(country_population, key=lambda x: x[1], reverse=True)

    # Get the top ten most populated countries
    top_ten_countries = sorted_countries[:10]

    return top_ten_countries

# Specify the file path for the countries_data.json file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/countries_data.json'  # Replace with the actual path to your file

# Call the function and get the results
ten_most_populated_countries = get_ten_most_populated_countries(file_path)

# Print the results
print("Ten Most Populated Countries:")
for country, population in ten_most_populated_countries:
    print(f"{country}: {population} population")




import re

def extract_email_addresses(file_path):
    # Open and read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Define a regular expression pattern for extracting email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to extract all email addresses from the text
    email_addresses = re.findall(email_pattern, text_content)

    return email_addresses

# Specify the file path for the email_exchange_big.txt file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/email_exchange_big.txt'  # Replace with the actual path to your file

# Call the function and get the list of email addresses
email_list = extract_email_addresses(file_path)

# Print the extracted email addresses
print("Extracted Email Addresses:")
for email in email_list:
    print(email)



