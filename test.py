from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
html = urlopen(url)

print(type(html))

bs = BeautifulSoup(html, "html.parser")
print(bs.prettify())

