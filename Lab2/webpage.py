from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://dantri.com.vn")
html_content = website.read().decode('utf-8')
website.close()
# html = urlopen("http://dantri.com.vn").read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
ul_news = soup.find('ul', 'ul1 ulnew')
li_news_list = ul_news.find_all('li')

for li in li_news_list:
    a_detail = li.h4.a
    title = a_detail['title']
    # print(li.prettify())
    content = a_detail.string
    print(content)
