from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re

AVERAGE_UAH = 14239
AVERAGE_BYN = 1442
AVERAGE_USD = 4552
AVERAGE_RUB = 54687

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Accept-Language': 'ru',
}


def parsing_data(byn, rub, usd):
    byn_r = requests.get(byn, headers=headers).text
    rub_r = requests.get(rub, headers=headers).text
    usd_r = requests.get(usd, headers=headers).text

    soup1 = BeautifulSoup(byn_r, 'lxml')
    clear_byn = soup1.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

    soup2 = BeautifulSoup(rub_r, 'lxml')
    clear_rub = soup2.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

    soup3 = BeautifulSoup(usd_r, 'lxml')
    clear_usd = soup3.find('span', {"class": "DFlfde SwHCTb"}).contents[0]
    return clear_byn, clear_rub, clear_usd


def conversion_string_data_in_float(clear_byn, clear_rub, clear_usd):
    float_byn = float(re.sub(",", ".", clear_byn))
    float_rub = float(re.sub(",", ".", clear_rub))
    float_usd = float(re.sub(",", ".", clear_usd))
    return float_byn, float_rub, float_usd


def calculation_number_of_pants_in_average(float_byn, float_rub, float_usd):
    count_pants_byn = AVERAGE_BYN / float_byn
    count_pants_rub = AVERAGE_RUB / float_rub
    count_pants_usd = AVERAGE_USD / float_usd
    count_pants_uah = AVERAGE_UAH / 40
    return int(count_pants_byn), int(count_pants_rub), int(count_pants_usd), int(count_pants_uah)


def first_page(request):
    passing = parsing_data('https://clck.ru/Z5uPQ', 'https://clck.ru/Z4Ax3', 'https://clck.ru/Z4Avo')
    return render(request, './main.html', {'byn': conversion_string_data_in_float(*passing)[0],
                                           'rub': conversion_string_data_in_float(*passing)[1],
                                           'usd': conversion_string_data_in_float(*passing)[2],
                                           'conversion_uah': calculation_number_of_pants_in_average(
                                               *conversion_string_data_in_float(*passing))[3],
                                           'conversion_byn': calculation_number_of_pants_in_average(
                                               *conversion_string_data_in_float(*passing))[0],
                                           'conversion_rub': calculation_number_of_pants_in_average(
                                               *conversion_string_data_in_float(*passing))[1],
                                           'conversion_usd': calculation_number_of_pants_in_average(
                                               *conversion_string_data_in_float(*passing))[2],
                                           })
