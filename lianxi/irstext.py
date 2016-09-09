#-*- coding:utf-8 -*-
import urllib2
import jieba
from bs4 import BeautifulSoup

class irsText:
    def getPageCode(self,url):
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            pageCode = response.read()

            bs = BeautifulSoup(pageCode)
            result = bs.findAll('p')

            text = ''

            for p in result:
                text += p.get_text()
                text += '\n'
                print text
            return text
        except urllib2.HTTPError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print u'不存在',e.reason

    def word_frequency(self,text):
        from collections import Counter

        words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
        c = Counter(words)
        for xx in c:
            print xx

        for word_freq in c.most_common(10):#获取排名前十的高频词,分别显示词名称与词数量.
            word, freq = word_freq
            print (word, freq)

url = 'http://iranshao.com/articles/2447-adidas-energy-boost-3-unboxing'
irsTextword = irsText()
irsTextword.getPageCode(url)
irsTextword.word_frequency(irsTextword.getPageCode())