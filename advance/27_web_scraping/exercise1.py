import json
import os
import html_to_json
import requests
from bs4 import BeautifulSoup

url:str = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

if response.status_code == 200:
    print('all ok')
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    print(soup.body)
    if not os.path.exists('web.json'):
        with open('web.json', 'w') as fileScrap:
            html_string = html_to_json.convert(str(soup.body))
            print(html_string)
            json.dump(html_string,fileScrap,ensure_ascii=False,indent=4)