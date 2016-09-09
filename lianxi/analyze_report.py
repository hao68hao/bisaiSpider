# -*- coding:utf-8 -*-
import jieba
import urllib2
import requests
from BeautifulSoup import BeautifulSoup


def extract_text(url):
    """导出html的内容"""
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    page = response.read()

    bs_source = BeautifulSoup(page)
    report_text = bs_source.findAll('p')



    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'
        print text
    return text

def word_frequency(text):
    """进入中文精确分词操作"""
    from collections import Counter

    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)
    # for xx in c:
    #     print xx

    for word_freq in c.most_common(10):#获取排名前十的高频词,分别显示词名称与词数量.
        word, freq = word_freq
        print (word, freq)

url = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
text_2016 = extract_text(url)
word_frequency(text_2016)