import sklearn
print(sklearn.__version__)


import pandas as pd

# Read the Hacker News CSV file (replace 'hacker_news.csv' with the actual file path)
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/hacker_news.csv'
df = pd.read_csv(file_path)

# Count the number of lines containing 'python' or 'Python'
python_lines = df[df['title'].str.contains('python|Python', na=False, case=False)]
count_python_lines = len(python_lines)

# Count the number of lines containing 'JavaScript', 'javascript', or 'Javascript'
javascript_lines = df[df['title'].str.contains('JavaScript|javascript|Javascript', na=False)]
count_javascript_lines = len(javascript_lines)

# Count the number of lines containing 'Java' but not 'JavaScript'
java_lines = df[df['title'].str.contains('Java', na=False) & ~df['title'].str.contains('JavaScript', na=False)]
count_java_lines = len(java_lines)

# Print the results
print(f'a) Count of lines containing python or Python: {count_python_lines}')
print(f'b) Count of lines containing JavaScript, javascript, or Javascript: {count_javascript_lines}')
print(f'c) Count of lines containing Java and not JavaScript: {count_java_lines}')

