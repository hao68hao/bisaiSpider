#-*- coding:utf-8 -*-

import urllib

def demoRetrieve(a, b, c):
    '''
    回调函数
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件大小
    '''

    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

url = 'http://www.baidu.com'
localDoc = '/Users/fujingmac/lauda/code/google.html'
urllib.urlretrieve(url, localDoc, demoRetrieve)

def downloadDoc(e, d, f):
    doc = 100.0 * e * d / f
    if doc > 100.0:
        doc = 100
    print '%.2f%%' % doc

urlDown = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
localADD = '/Users/fujingmac/lauda/code/pythondoc.tar.bz2'
urllib.urlretrieve(urlDown, localADD, downloadDoc)



