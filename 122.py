'''import urllib.request

operner = urllib.request.build_opener()
response = operner.open('https://httpbin.org/get')

print(response.read())

import requests
response = requests('https://httpbin.org/get')

print(response.content)'''

'''
import urllib.request

operner = urllib.request.build_opener()
response = operner.open('https://httpbin.org/get')

print(response.read())

import requests
response = requests('https://httpbin.org/get')

print(response.content)'''

'''import requests
response = requests.get('https://httpbin.org/get')

print(response.text)
print(f'Datatype - {type(response.text)}')'''
'''
import requests
response = requests.post('https://httpbin.org/post', data = 'Test data', headers={'h1':'Test title'})

print(response.text)'''
'''
import requests
response = requests.post('https://httpbin.org/post', data = {'testform'})'''

import requests
res_parse_list=[]
response = requests.get('https://coinmarkercap.com')
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith('$'):
        for parse_elem_2 in parse_elem_1.split('</span'):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)

bitcoin_exchage_rate = res_parse_list[0]
print(bitcoin_exchage_rate)

from bs4 import BeautifulSoup
import requests

response=requests



