# import requests
# from bs4 import BeautifulSoup
# import csv
# import re


# # Function to make requests to the Netflix website and get the HTML content
# def get_netflix_html():
#     url = 'https://www.justwatch.com/uk/provider/netflix/movies'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers) # Make an HTTP GET request to the website
    
#     if response.status_code == 200:

#         return response.text
#     else:
#         print(F"Error: Unable to fetch Netflix website. Status code: {response.status_code}")
#         return None

# # Function to write HTML content to a text file for inspection
# def write_html_to_file(html_content, filename='netflix_html.txt'):
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(html_content)


# # Function to parse HTML content and extract movie information
# def parse_netflix_html(html_content):
    
#     # Regular expression pattern to extract movie titles
#     pattern = r'"name":"(.*?)"' #Pattern to capture movie name

#     # Extracting movie titles using regex
#     movie_titles = re.findall(pattern, html_content)

#     return movie_titles

# def main():
#     netflix_html = get_netflix_html()
#     write_html_to_file(netflix_html)

#     # if netflix_html:
#     #     # Get list
#     #     movies = parse_netflix_html(netflix_html)
#     #     for title in movies:
#     #         print(title)

# if __name__ == "__main__":
#     main()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to your chromedriver executable
webdriver_path = '/path/to/chromedriver'

# Start a Selenium webdriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Load the website
driver.get('https://www.justwatch.com/uk/provider/netflix/movies')

# Wait for the movies to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))

# Get the page source after all content is loaded
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find movie titles
movie_titles = soup.find_all('div', class_='title')

# Extract movie titles
for title in movie_titles:
    print(title.text.strip())

# Close the webdriver
driver.quit()
