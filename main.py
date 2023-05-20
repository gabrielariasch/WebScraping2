import bs4
import lxml #helps us process XML and HTML
from bs4 import BeautifulSoup
import requests

#Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
base_url = 'https://quotes.toscrape.com/page/1/'

res = requests.get(base_url)

soup = bs4.BeautifulSoup(res.text,'lxml')

#TASK: Get the names of all the authors on the first page.
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)
print(authors)

#TASK: Create a list of all the quotes on the first page.
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

#TASK: Inspect the site and extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
tags = set()
for tag in soup.select('.tag-item'):
    tags.add(tag.text)
print(tags)


#Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.

authors = set()
exercise_url = 'https://quotes.toscrape.com/page/{}/'

for n in range(1,11):
    scrape_url = exercise_url.format(n)
    res2 = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res2.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

print(authors)
print(len(authors))