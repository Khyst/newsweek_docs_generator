from bs4 import BeautifulSoup
import requests

html_file = "example.html"

with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

file.close()

soup = BeautifulSoup(html_content, "html.parser")

title = soup.title 
title_text = title.get_text()

print("title: ")
print(title_text, "\n")

articles_section = soup.find(id="v_article")
paragraphs = articles_section.find_all('p')

p_texts = [p.get_text() for p in paragraphs]

p_texts = p_texts[:-2]


for p_text in p_texts:
    print(p_text)
    print()


with open("article_0.txt", "w", encoding="utf-8") as file:
    file.write(title_text + "\n\n")
    
    for p_text in p_texts:
        file.write(p_text + "\n\n")