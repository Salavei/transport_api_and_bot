from django.http import HttpResponse
from django.shortcuts import render
import requests

api = 'f89fed0d4d207b879a2d'

byn = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_BYN&compact=ultra&apiKey={api}')
rub = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_RUB&compact=ultra&apiKey={api}')
usd = requests.get(f'https://free.currconv.com/api/v7/convert?q=UAH_USD&compact=ultra&apiKey={api}')


def first_page(request):
    info_bun = byn.json()['UAH_BYN']
    info_rub = rub.json()['UAH_RUB']
    info_usd = usd.json()['UAH_USD']
    return render(request, './main.html', {'byn': (int((info_bun * 40) * 100) / 100),
                                           'rub': (int((info_rub * 40) * 100) / 100),
                                           'usd': (int((info_usd * 40) * 100) / 100)
                                           })
