import requests
from bs4 import BeautifulSoup
#page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
#print("page: {0}".format(page))
#print("page.status_code: {0}".format(page.status_code))
#print("page.content: {0}".format(page.content))

soup = BeautifulSoup(page.content, 'html.parser')
#pretty_soup = soup.prettify()
#print(soup.prettify())
#print(soup.find_all('p', class_='outer-text'))
#print(soup.find_all(class_="outer-text"))
print(soup.find_all(id="first"))
#print("********list: {0}".format(list(soup.children)))
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
#print(page.status_code)
#print(page.content)
#print(page.prettify())
#easrdfxtgh