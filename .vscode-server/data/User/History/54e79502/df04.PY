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
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/melana_trump_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")



