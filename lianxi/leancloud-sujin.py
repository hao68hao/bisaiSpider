# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ISuJin:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self, pageIndex):
        url = 'http://isujin.com/page/' + str(pageIndex)
        req = requests.get(url, headers=self.headers)
        return req

    def getItem(self, pageIndex):
        req = self.getPage(pageIndex)
        if req.status_code == 200:
            print '第', pageIndex, '页下载完成'
            soup = BeautifulSoup(req.content, 'html.parser')
            for link in soup.find_all('div', 'post'):
                title = link.a['title']
                ids = link.a['data-id']
                imgUrl = link.a.contents[1]['src']
                jieshao = link.find_all('p')[1].string
                detailUrl = link.a['href']
                detail = self.getDetailContent(link.a['href'])
                print title, ids, imgUrl, jieshao, detailUrl, detail

    def getDetailContent(self, detailUrl):
        string = ''
        reqcontent = requests.get(detailUrl)
        detailContentSoup = BeautifulSoup(reqcontent.content, 'html.parser')
        for s in detailContentSoup.find('div', 'content').p.stripped_strings:
            string = string + s + '\n'
        return string

    def start(self):
        nowPage = 1
        while nowPage <= 4:
            nowPage += 1
            self.getItem(nowPage)
            # file = open("sujin.txt", 'w')
            # file.write(self.getItem(nowPage))

dfefd = ISuJin()
dfefd.start()

