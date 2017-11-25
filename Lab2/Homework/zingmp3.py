from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://nhaczingmp3.com/")
html_content = website.read().decode('utf-8')
website.close()

soup = BeautifulSoup(html_content, "html.parser")
print(soup.prettify())
