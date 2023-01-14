import requests
from bs4 import BeautifulSoup

AVERAGE_UAH = 14239
AVERAGE_BYN = 1442
AVERAGE_USD = 4552
AVERAGE_RUB = 54687

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    'Accept-Language': 'by'
}

URL_DICT = {
    'byn': 'https://minfin.com.ua/currency/converter/40-uah-to-byn/',
    'rub': 'https://minfin.com.ua/currency/converter/40-uah-to-rub/',
    'usd': 'https://minfin.com.ua/currency/converter/40-uah-to-usd/'
}

NAME_MONEY = ['byn', 'rub', 'usd']


def parse_money():
    raw_exchange_money = parsing_data(url_dict=URL_DICT)
    exchange_money_dict = {NAME_MONEY[i]: float(raw_exchange_money[i]) for i in range(len(raw_exchange_money))}
    average_salary = calculation_number_of_pants_in_average(exchange_money_dict)
    return exchange_money_dict, average_salary


def parsing_data(url_dict) -> list:
    raw_currency = []
    for currency in url_dict.values():
        soup_find = BeautifulSoup(requests.get(currency, headers=HEADERS).text, 'lxml')
        raw_currency.append(soup_find.findAll('label', {"class": "sc-11fozao-2 heSTnT"})[1].find('input').get('value'))
    return raw_currency


def calculation_number_of_pants_in_average(exchange_money_dict: dict) -> dict:
    conversion = {
        'conversion_uah': int(AVERAGE_UAH / 40),
        'conversion_byn': int(AVERAGE_BYN / exchange_money_dict.get('byn')),
        'conversion_rub': int(AVERAGE_RUB / exchange_money_dict.get('rub')),
        'conversion_usd': int(AVERAGE_USD / exchange_money_dict.get('usd')),
    }
    return conversion
