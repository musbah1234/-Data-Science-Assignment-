def count_lines_and_words(obama_speech):
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
file_path = 'obama_speech.txt'

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
