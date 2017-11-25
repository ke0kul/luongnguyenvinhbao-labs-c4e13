from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode('utf-8')
website.close()

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', id = "tableContent")

# temp = open('temp.html', 'w')
# tem.write(table_date.prettify())
# temp.close()

trs = table.find_all('tr')
data_list = []

for tr in trs:
    tds = tr.find_all('td')
    data = {}
    for index, td in enumerate(tds):
        content = td.string
        if content != None:
            if index == 0:
                data['title'] = content.strip()
            elif index == 1:
                data['Quy 4/2016'] = content
            elif index == 2:
                data['Quy 1/2017'] = content
            elif index == 3:
                data['Quy 2/2017'] = content
            elif index == 4:
                data['Quy 3/2017'] = content
    if data != {}:
        data_list.append(data)
print(data_list)
