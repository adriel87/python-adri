import requests
from bs4 import BeautifulSoup

url:str = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

if response.status_code == 200:
    print('all ok')
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    print(soup.title)
    print(soup.title.get_text())
    print(soup.s)

    tables = soup.find_all('table', {'cellpadding':'3'})

    table = tables[0]

    for td in table.find('tr').find_all('td'):
        print(td.text)