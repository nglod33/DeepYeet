import requests
from bs4 import BeautifulSoup
import json
import collections

import http.client, urllib.request, urllib.parse, urllib.error, base64
'''
Enter a query to search
Return a list of results
Choose a product (from names)
Return sku,
'''
def format(link):
    formatted = requests.get(link)
    formatted = json.loads(formatted.text)
    return formatted

def test(QUERY):
    url = 'https://api.wegmans.io//products/search?query=milk&results=100&page=1&api-version=2018-10-18&subscription-key=cab190ce1e6e461f8c4c29ea91c3b976'
    server = 'https://api.wegmans.io/'
    path = 'products/search?query='
    #query
    page = "&results=100&page="
    #page_num
    #(doesn't work in this line bc not referenced yet) print(formatted['pages']) # # of pages
    api_ver = '&api-version=2018-10-18&'
    sub_key = 'subscription-key=cab190ce1e6e461f8c4c29ea91c3b976'
    #query_str = 'milk'
    #pag_num = '0'
    #url_template = server + path + QUERY + page+ PAGE_NUM + api_ver + sub_key
    formatted = format(url)
    #loops for each list of products (value is number of pages)
    data = {}
    for counter1, PAGE_NUM in enumerate(range(formatted['pages'])):
        url_template = server + path + QUERY + page + str(PAGE_NUM) + api_ver + sub_key
        #loops for each product entry (results has all product dicts)
        for counter2, product in enumerate(range(len(formatted['results']))):
            #loops for each part of the entry (list_entry = str: sku, name, _links)
            list = [formatted['results'][product][list_entry] for list_entry in formatted['results'][product]]
            sku, name, links = [list[i] for i in range(3)]
            #_links: self, locations, availibilities, prices in list
            link_self, link_loc, link_avail, link_price = [links[i]['href'] for i in range(4)]
            data[name] = [sku, link_self, link_loc, link_avail, link_price]
    return data



def getSelf(link_self):
    formatted = format(server + link_self + sub_key)
def getLoc(link_loc):
    formatted = format(server + link_loc + sub_key)
def getAvail(link_avail):
    formatted = format(server + link_avail + sub_key)
def getPrice(link_prices):
    formatted = format(server + link_prices + sub_key)
'''
            product_url = formatted['results'][product][list_entry][0]['href']
            try:
                print(product_url)
                #access product url
            except:
                print('FAIL', 'abc',formatted['results'][product])
                continue
            if dict == '_links': #self, location, availibility, price,
                for i in formatted['results'][product]['_links']:
                    #print("\n\n"+str(i)+"\n\n")
                    new_path = formatted['results'][product]['_links'][0]
                    product_url = server + new_path + sub_key
                    fproduct_url = format(product_url)
                    print(fproduct_url)
                    '''
            #list_products.add(formatted['results'][product]['name'])
    #Format is dict (Length 100 for actual values), int pages, dict (Length 1 for next page)

    #print(len(formatted['results'])) #100
    #print(formatted['results'][0]) #results

    #rint(len(formatted['_links'])) #1
    #print(formatted['_links'][0]) #next page

'''
for counter, i in enumerate(formatted):
    if int(counter) < 20:
        print(len(formatted))
        print(counter)
        print(counter, formatted['results'][counter])
        print('AHHHHHHHHH')'''
    #print(formatted['results'][0])
    #print(formatted['results'][0]['sku'])
    #print(formatted['results'][0]['name'])
print(test('milk'))

'''
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Subscription-Key': 'cab190ce1e6e461f8c4c29ea91c3b976',
}

params = urllib.parse.urlencode({
    # Request parameters
    'results': '100',
    'page': '1',
    'query': 'milk'
})

try:
    conn = http.client.HTTPSConnection('api.wegmans.io')
    conn.request('GET', '/products/search?query={query}&api-version=2018-10-18&%s' % params, '{body}', headers)
    response = conn.getresponse()
    data = response.read()
    for counter, i in enumerate(range(10)):
        print(counter, str(data)[i])
    print(len((data)))
    conn.close()
except Exception as e:
    print('[Errno {0}] {1}'.format(e.errno, e.strerror))
'''
