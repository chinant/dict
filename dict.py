#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys, re, pdb
from urllib.request import urlopen, Request
from urllib.parse import quote

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'

headers = {'User-Agent': user_agent}

data = {}

if len(sys.argv) != 2:
    print('usage: %s <word>' % sys.argv[0])
else:
    word = re.sub(' ', '_', sys.argv[1]) #enable translate a sentence
    req = Request('http://www.iciba.com/%s' % quote(word),data,headers)
    html = urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    context = soup.find("div", class_="in-base")
    if context is None:
        print('Sorry, cannot translate the word(s)')
    else:
        rows = context.find_all("li", class_="clearfix")
        for row in rows:
            result = re.sub('\n', ' ', row.text)
            result = re.sub('&nbsp;', ' ', result)
            result = re.sub(r'\s+', ' ', result)
            print(result.strip())
