#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
import json
from urllib.request import urlopen, Request
from urllib.parse import quote

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'

headers = {'User-Agent': user_agent}

data = {}

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


if len(sys.argv) < 2:
    print('usage: %s <word>' % sys.argv[0])
else:
    # word = re.sub('%20', '_', sys.argv[1]) #enable translate a sentence
    word = '%20'.join(sys.argv[1:]) #enable translate a sentence
    req = Request('http://iciba.com/word?w=%s' % quote(word),data,headers)

    try:
        html = urlopen(req).read().decode('utf8')
    except Exception:
        raise("HTTPException")
    
    res_main = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
    main = re.findall(res_main,  html,re.S|re.M)
   
    data = json.loads(main[0])

    if 'props' in data.keys() and 'symbols' in data['props']['initialDvaState']['word']['wordInfo']['baesInfo']:
        symbols = data['props']['initialDvaState']['word']['wordInfo']['baesInfo']['symbols']
        if (symbols):
            print("英["+symbols[0]['ph_en'] + "]", "美["+symbols[0]['ph_am'] +"]")

            for part in symbols[0]['parts']:
                print(part['part'].ljust(3,' '), part['means'])
    else:
        print('Sorry, cannot translate the word(s)')
