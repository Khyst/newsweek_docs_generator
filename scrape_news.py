import requests
from bs4 import BeautifulSoup
import time

# URL of the webpage to scrape
url = "https://www.newsweek.com/who-would-better-president-working-class-opinion-1948661"

# Send a GET request to the webpage
response = requests.get(url)


print(response.content)

# Wait for the webpage to load
time.sleep(5)  # Adjust the sleep duration as needed

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")

    # TODO: Write your scraping logic here

else:
    print("Failed to retrieve webpage:", response.status_code)