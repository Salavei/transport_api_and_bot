import requests
from bs4 import BeautifulSoup
import re

AVERAGE_UAH = 14239
AVERAGE_BYN = 1442
AVERAGE_USD = 4552
AVERAGE_RUB = 54687
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Accept-Language': 'ru',
}


def parsing_data(byn, rub, usd) -> list:
    raw_currency = []
    for currency in (byn, rub, usd):
        soup_find = BeautifulSoup(requests.get(currency, headers=HEADERS).text, 'lxml')
        raw_currency.append(soup_find.find('span', {"class": "DFlfde SwHCTb"}).contents[0])
    return raw_currency


def conversion_string_data_in_float(raw_currency: list) -> dict:
    done_float_currency = {
        'byn': float(re.sub(",", ".", raw_currency[0])),
        'rub': float(re.sub(",", ".", raw_currency[1])),
        'usd': float(re.sub(",", ".", raw_currency[2]))
    }
    return done_float_currency


def calculation_number_of_pants_in_average(done_float_currency: dict) -> dict:
    conversion = {
        'conversion_uah': int(AVERAGE_BYN / 40),
        'conversion_byn': int(AVERAGE_BYN / done_float_currency.get('byn')),
        'conversion_rub': int(AVERAGE_RUB / done_float_currency.get('rub')),
        'conversion_usd': int(AVERAGE_USD / done_float_currency.get('usd')),
    }
    return conversion
