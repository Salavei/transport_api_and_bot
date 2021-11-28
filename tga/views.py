from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

byn = 'https://clck.ru/Z5uPQ'
rub = 'https://clck.ru/Z4Ax3'
usd = 'https://clck.ru/Z4Avo'
bun_r = requests.get(byn, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Accept-Language': 'ru',
})
rub_r = requests.get(rub, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept-Language': 'en-US',
})
usd_r = requests.get(usd, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept-Language': 'fr-CA',
})
html_bun = bun_r.text
html_rub = rub_r.text
html_usd = usd_r.text

soup1 = BeautifulSoup(html_bun, 'lxml')
take_for_was_and_now = soup1.find_all('div', {"class": "main"})
clear_bun = soup1.find('span', {"class": "DFlfde SwHCTb"})
# clear_bun = soup1.find('span', {"class": "DFlfde SwHCTb"}) .contents[0]

soup2 = BeautifulSoup(html_rub, 'lxml')
take_for_was_and_now1 = soup2.find_all('div', {"class": "main"})
clear_rub = soup2.find('span', {"class": "DFlfde SwHCTb"})
# clear_rub = soup2.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

soup3 = BeautifulSoup(html_usd, 'lxml')
take_for_was_and_now2 = soup3.find_all('div', {"class": "main"})
clear_usd = soup3.find('span', {"class": "DFlfde SwHCTb"})
# clear_usd = soup3.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

def first_page(request):
    return render(request, './main.html', {'byn': clear_bun,
                                           'rub': clear_rub,
                                           'usd': clear_usd,
                                           })
