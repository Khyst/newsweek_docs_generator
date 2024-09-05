from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import time
import os, sys

options = webdriver.ChromeOptions()

service = Service(executable_path=r'C:/Users/LG/chrome_driver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

URL = "https://www.newsweek.com/opinion"

driver.get(URL)

# Find the X button using CSS selector
# x_button = driver.find_element_by_css_selector("#sailthru-overlay-container > div.sailthru-overlay.sailthru-overlay-animation > button")

# Click the X button
# x_button.click()

# Get the HTML content of the page
html = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Find the first element using CSS selector
first_element = soup.select_one("body > div.main.container-fluid > div:nth-child(4)")

with open("article_0.txt", "w", encoding="utf-8") as file:
    file.write(first_element.get_text())

# Select all elements using CSS selector
all_elements = soup.select("body > div.main.container-fluid > div:nth-child(2) > article.col-sm-3")

# Write the text content of each element to separate files
for i, element in enumerate(all_elements):
    with open(f"article_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(element.get_text())

# second_element = soup.select_one("body > div.main.container-fluid > div:nth-child(2) > article.item-1.col-sm-3")
# # print(secpmd_element.get_text())
# with open("secpmd_articles.txt", "w", encoding="utf-8") as file:
#     file.write(second_element.get_text())


# third_element = soup.select_one("body > div.main.container-fluid > div:nth-child(2) > article.item-2.col-sm-3")
# # print(third_element.get_text())
# with open("third_articles.txt", "w", encoding="utf-8") as file:
#     file.write(third_element.get_text())

# fourth_element = soup.select_one("body > div.main.container-fluid > div:nth-child(2) > article.item-3.col-sm-3")
# # print(fourth_element.get_text())
# with open("fourth_articles.txt", "w", encoding="utf-8") as file:
#     file.write(fourth_element.get_text())

# fifth_element = soup.select_one("body > div.main.container-fluid > div:nth-child(2) > article.item-4.col-sm-3")
# # print(fifth_element.get_text())
# with open("fifth_articles.txt", "w", encoding="utf-8") as file:
#     file.write(fifth_element.get_text())

# sixth_element = soup.select_one("body > div.main.container-fluid > div:nth-child(5)")
# # print(sixth_element.get_text())
# with open("sixth_articles.txt", "w", encoding="utf-8") as file:
#     file.write(sixth_element.get_text())

# Close the browser
driver.quit()