import bs4 as bs
import urllib.request
import requests

sauce= urllib.request.urlopen('https://www.ethicalconsumer.org/ethicalcampaigns/boycotts').read()
soup=bs.BeautifulSoup(sauce,'lxml')
print(soup.find_all('h3'))

# for item in soup.find_all('div'):
#     print(item.get('b'))

# for item in soup.find_all('h3'):
#     for item1 in soup.find_all('div'):
#         print(item1)

