import requests
from bs4 import BeautifulSoup
import json

# URL of the website
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information from the webpage
    # (Replace this part with your specific scraping requirements)
    data_to_scrape = {
        "title": soup.title.text,
        "paragraphs": [p.text.strip() for p in soup.find_all('p')]
        # Add more data extraction as needed
    }

    # Store the scraped data as a JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_to_scrape, json_file, ensure_ascii=False, indent=2)

    print('Data scraped and stored successfully as "scraped_data.json".')
else:
    print(f'Error: Unable to fetch data. Status code: {response.status_code}')
