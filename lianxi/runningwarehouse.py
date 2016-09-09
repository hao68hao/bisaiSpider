#-*- coding:utf-8 -*-
import urllib2
import re
import sys
# import chardet
import torndb
import requests
import BeautifulSoup
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")
db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

try:
    url = 'http://www.runningwarehouse.com/catpage-HOKAM.html'
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
    response = requests.get(url, headers=header)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.body.find_all(href=re.compile(r'HOKA_ONE_ONE'))
    for url in urls:
        if url['href'].find('descpage') == -1:
            continue
        detail_response = requests.get(url['href'],headers=header)
        detail_html = detail_response.text
        detail_soup = BeautifulSoup(detail_html, 'html.parser')
        name = detail_soup.body.h1.string
        price = detail_soup.body.div.find_all("span", attrs={"class": "price"})[0].string

        divs = detail_soup.body.div.find_all("div", attrs={"class": "left_column fl"})
        details = ""
        for div in divs:
            ps = div.find_all("p")
            for p in ps:
                details += p.string

        divs = detail_soup.body.find_all("div", attrs={"class": "right_column fr"})
        weight = divs[0].find_all("p")[1].contents[1].split(" ")[1]

        file = open("hoka.txt", "w")
        file.write(name)

        print name
        print price
        print weight
        print details

except urllib2.HTTPError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print u"连接网页失败", e.reason




# def torndbConn(self,shose):
#     try:
#         exe = "insert into runningwarehouse(name,price,weight,details) values ('%(name)s', '%(price)s', '%(weight)s', '%(details)s')" % dict(
#             name=shose[0].strip(),
#             price=shose[1].strip(),
#             weight=shose[2].strip(),
#             details=shose[3].strip())
#         print exe
#         db.execute(exe)
#     except Exception as e:
#         print (e)

















