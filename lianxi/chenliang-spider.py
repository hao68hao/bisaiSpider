#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import socket
import base64
import urllib2
import cookielib
import datetime

MAIL_CONFIG = ('10.100.27.122', 10001)
APP_NAME = 'bbs'
#APP_NAME = 'ottmanager'

LOCAL_IP = socket.gethostbyname(socket.gethostname())
socket.setdefaulttimeout(30)

def mail(msg, msg_level='info', msg_type='text', app_name=APP_NAME):
        pass
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    if msg_type == 'text':
#        msg = '======</p>Datetime：%s<p>From: %s</p>%s<p>======' % \
#              (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), LOCAL_IP, msg)
#    try:
#        sock.connect(MAIL_CONFIG)
#        sock.send('#|#'.join([app_name, msg_level, msg_type, base64.b64encode(msg)]))
#    except Exception as e:
#        print "mail error ", e
#    finally:
#        print msg
#        sock.close()

def http_get(url):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
               "Accept": "text/plain"}
    print "http_get", url
    req = urllib2.Request(url, headers=i_headers)
    try:
      page = urllib2.urlopen(req)
      return page.read()
    except urllib2.HTTPError, e:
      print "Error Code:", e
      return None
    except urllib2.URLError, e:
      print "Error Reason:", e
      return None
    except Exception as e:
      print "http_get error:", e
      return None

def http_post(url, data):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
               "Accept": "text/plain"}
    req = urllib2.Request(url, headers=i_headers)
    try:
      page = urllib2.urlopen(req, data)
      return page.read()
    except urllib2.HTTPError, e:
      print "Error Code:", e
    except urllib2.URLError, e:
      print "Error Reason:", e
    except Exception as e:
      print "http_get error:", e

def get_bbs_first_page_info():
    result = []
    for i in xrange(1, 2):
        url="http://bbs.yj.youku.com/forum.php?mod=forumdisplay&fid=111&orderby=dateline&filter=author&sort_specialtype=%E5%8F%91%E5%B8%96%E6%97%B6%E9%97%B4&orderby=dateline&page={page}".format(page=i)
        html = http_get(url)
        if not html:
            continue
        html = html.replace("\r", "")
        html = html.replace("\n", "")
        html = html.replace("\t", "")
        matchcontext = re.compile('<tbody (.+?)</tbody>', re.DOTALL).findall(html)
        for tbody in matchcontext:
            infos = re.compile('</em>(.+?)<a href="(.+?)" (.+?)>(.+?)</a>').findall(tbody)
            if infos:
                result.append((infos[0][3], infos[0][1].replace("amp;", "")))
    return result

def get_bbs_answer_page_info():
    result = []
    for i in xrange(1, 2):
        url="http://bbs.yj.youku.com/forum.php?mod=forumdisplay&fid=111&page={page}".format(page=i)
        html = http_get(url)
        if not html:
            continue
        html = html.replace("\r", "")
        html = html.replace("\n", "")
        html = html.replace("\t", "")
        matchcontext = re.compile('<tbody (.+?)</tbody>', re.DOTALL).findall(html)
        for tbody in matchcontext:
            infos = re.compile('</em>(.+?)<a href="(.+?)" (.+?)>(.+?)</a>').findall(tbody)
            if infos:
                result.append((infos[0][3], infos[0][1].replace("amp;", "")))
    return result

def get_bbs_page_diff(current, last):
    result = []
    if not current or not last:
        return result
    last_set = set()
    current_set = set()
    for l in last: last_set.add(l[1])
    for c in current: current_set.add(c[1])
    diffs = current_set.difference(last_set)
    print "get_bbs_page_diff", diffs, "current", current, "last_set", last_set
    for diff in diffs:
        for c in current:
            if c[1] == diff:
                result.append(c)
                break
    return result

def send_new_bbs_page(last_info):
    page_info = get_bbs_first_page_info()
    if page_info:
        diffs = get_bbs_page_diff(page_info, last_info)
        for diff in diffs:
            title = diff[0]
            url = "http://bbs.yj.youku.com/" + diff[1]
            mail("新贴子 <a href=%s>%s</a>" % (url, title))
    return page_info

def send_answer_bbs_page(last_info):
    page_info = get_bbs_answer_page_info()
    if page_info:
        diffs = get_bbs_page_diff(page_info, last_info)
        for diff in diffs:
            title = diff[0]
            url = "http://bbs.yj.youku.com/" + diff[1]
            mail("新回复 <a href=%s>%s</a>" % (url, title))
    return page_info

def main():
    last_info = None
    last_answer = None
    mail_items = []
    start_time = time.time()
    while True:
        last_info_temp = send_new_bbs_page(last_info)
        last_answer_temp = send_answer_bbs_page(last_answer)
        if last_info_temp is not None:
            last_info = last_info_temp
        if last_answer_temp is not None:
            last_answer = last_answer_temp
        time.sleep(120)

if __name__ == "__main__":
    main()
