from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re


def parsing_data(byn, rub, usd):
    byn_r = requests.get(byn, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ru',
    })
    rub_r = requests.get(rub, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ru',
    })
    usd_r = requests.get(usd, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
        'Accept-Language': 'ru',
    })
    html_byn = byn_r.text
    html_rub = rub_r.text
    html_usd = usd_r.text

    soup1 = BeautifulSoup(html_byn, 'lxml')
    clear_byn = soup1.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

    soup2 = BeautifulSoup(html_rub, 'lxml')
    clear_rub = soup2.find('span', {"class": "DFlfde SwHCTb"}).contents[0]

    soup3 = BeautifulSoup(html_usd, 'lxml')
    clear_usd = soup3.find('span', {"class": "DFlfde SwHCTb"}).contents[0]
    return clear_byn, clear_rub, clear_usd


def conversion_string_data_in_float(clear_byn, clear_rub, clear_usd):
    change_in_int_byn = re.sub(",", ".", clear_byn)
    change_in_int_rub = re.sub(",", ".", clear_rub)
    change_in_int_usd = re.sub(",", ".", clear_usd)
    float_byn = float(change_in_int_byn)
    float_rub = float(change_in_int_rub)
    float_usd = float(change_in_int_usd)
    return float_byn, float_rub, float_usd


def calculation_number_of_pants_in_average(float_byn, float_rub, float_usd):
    average_salary_uah = 14239
    average_salary_byn = 1442
    average_salary_usd = 4552
    average_salary_rub = 54687
    count_pants_byn = average_salary_byn / float_byn
    count_pants_rub = average_salary_rub / float_rub
    count_pants_usd = average_salary_usd / float_usd
    count_pants_uah = average_salary_uah / 40
    return int(count_pants_byn), int(count_pants_rub), int(count_pants_usd), int(count_pants_uah)


passing = parsing_data('https://clck.ru/Z5uPQ', 'https://clck.ru/Z4Ax3', 'https://clck.ru/Z4Avo')
done_conversion = conversion_string_data_in_float(*passing)
done_calculation_pants = calculation_number_of_pants_in_average(*done_conversion)


def first_page(request):
    byn = done_conversion[0]
    rub = done_conversion[1]
    usd = done_conversion[2]
    conversion_byn = done_calculation_pants[0]
    conversion_rub = done_calculation_pants[1]
    conversion_usd = done_calculation_pants[2]
    conversion_uah = done_calculation_pants[3]
    return render(request, './main.html', {'byn': byn,
                                           'rub': rub,
                                           'usd': usd,
                                           'conversion_uah': conversion_uah,
                                           'conversion_byn': conversion_byn,
                                           'conversion_rub': conversion_rub,
                                           'conversion_usd': conversion_usd,
                                           })
