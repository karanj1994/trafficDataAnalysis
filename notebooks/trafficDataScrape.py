# https://www.dataquest.io/blog/web-scraping-tutorial-python/ - reference for Beautiful Soup Training

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
