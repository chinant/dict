#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys, re, pdb
from urllib.request import urlopen

if len(sys.argv) != 2:
    print('usage: %s <word>' % sys.argv[0])
else:
    word = re.sub(' ', '_', sys.argv[1]) #enable translate a sentence
    html = urlopen('http://www.iciba.com/%s' % word).read().decode('utf8')
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