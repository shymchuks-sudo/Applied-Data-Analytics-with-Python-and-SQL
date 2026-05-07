from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.wikipedia.org')
soup = BeautifulSoup(req.content, 'html.parser')
soup.prettify()
# the Beautiful Soup's method ​prettify is used to actually
# ​convert the Beautiful Soup tree into a formatted string

hdr = {'User-Agent': 'Mozilla/5.0'}
r = requests.get('https://www.goodreads.com/', headers = hdr)
# print(r.status_code)
# 200
r = requests.get('https://www.goodreads.com/')
# print(r.status_code)
# 403

book_soup = BeautifulSoup(r.content, 'html.parser')
categories = book_soup.find_all('a', attrs={'class': 'gr-hyperlink'})
# print(categories)

txt_categories = []
for tag in categories:
    if 'genres' in tag.get('href'):
        txt_categories.append(tag.string)

for cat in txt_categories:
    print(cat)
