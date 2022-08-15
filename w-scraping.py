                               
from bs4 import BeautifulSoup

import requests

print(' _______   _______   ______   ______    ______   __    __   _______ ')
print(' /       \ /       \ /      \ |      \  /      \ |  \  |  \ /       ')
print('|  $$$$$$$|  $$$$$$$|  $$$$$$\ \$$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$$')
print(' \$$    \ | $$      | $$   \$$/      $$| $$  | $$| $$  | $$ \$$    \ ')
print(' _\$$$$$$\| $$_____ | $$     |  $$$$$$$| $$__/ $$| $$__/ $$ _\$$$$$$')
print('|       $$ \$$     \| $$      \$$    $$| $$    $$ \$$    $$|       $$')
print(' \$$$$$$$   \$$$$$$$ \$$       \$$$$$$$| $$$$$$$   \$$$$$$  \$$$$$$$ ')
print('                                       | $$                          ')
print('                                       | $$                          ')
print('                                        \$$                          ') >
print('created by @pusprimordial')

print('')

print('Web-scraping simples usando beautiful-soup')
print('HTML-SCRAP.')
print('')


print('Digite um endereço: (ex: https://mysite.com)')
url = input()

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())

