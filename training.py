import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
#print("page: {0}".format(page))
#print("page.status_code: {0}".format(page.status_code))
#print("page.content: {0}".format(page.content))

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
print("list: {0}".format(list(soup.children)))