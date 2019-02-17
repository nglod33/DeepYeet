from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.ethicalconsumer.org/ethicalcampaigns/boycotts')
soup = BeautifulSoup(site.text,'html.parser')
results = soup.find_all('h3')
results = soup.find_all('p')
for counter, i in enumerate(results):
    print(counter, i)
