import requests
import re

url = raw_input('Digite o site que deseja fazer o teste: ')

padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)

injecao = padrao.groups()[0] + '\''

print (injecao)

header = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
          'AppleWebKit/537.36 (KHTML, like Gecko) '
          'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(injecao, headers=header)

html = req.text

if 'mysql_fetch_array()' in html or 'You have an error in your SQL syntax' in html:
    print (' Site Vulneravel a SQLInjection')
else:
    print (' Site A PRINCIPIO Nao Vulneravel a SQLInjection ')
