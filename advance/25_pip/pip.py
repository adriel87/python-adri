import requests
import re

url = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(url)

if response.status_code == 200:
    
    regex = r'\\+[r|n]'
    copy_whitout = re.sub('\n','',response.text.upper())
    copy_whitout = re.sub('\r', '', copy_whitout)
    copy_whitout = re.sub('\W', ' ',copy_whitout)
    words_set = set(copy_whitout.split(' '))
    dct=[]
    for word in list(words_set):
        dct.append({'word':word, 'count':copy_whitout.count(word)})

    print(sorted(dct,key=lambda a: a['count'],reverse=True))
    