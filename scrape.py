import requests
from bs4 import BeautifulSoup
import json


URL = "https://news.mit.edu/topic/women-stem"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

jsonobj = []
article_elements = soup.find_all("article", class_="term-page--news-article--item")

for article in article_elements:
    title = article.find("span", attrs={"itemprop": "name headline"}).text
    link = "news.mit.edu" + article.find("a", class_="term-page--news-article--item--title--link").get('href')
    desc = article.find("p", class_="term-page--news-article--item--dek").text
    date = article.find("p", class_="term-page--news-article--item--publication-date").text
    jsonobj.append({'title': title, 'link': link, 'desc': desc, 'date': date})

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(jsonobj, f, ensure_ascii=False, indent=4)


    