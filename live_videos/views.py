from django.shortcuts import render
from .utils.business_logic import parsing_data, conversion_string_data_in_float, calculation_number_of_pants_in_average


def pants_page(request):
    raw_currency = parsing_data('https://clck.ru/Z5uPQ', 'https://clck.ru/Z4Ax3', 'https://clck.ru/Z4Avo')
    context = {**conversion_string_data_in_float(raw_currency),
               **calculation_number_of_pants_in_average(conversion_string_data_in_float(raw_currency))}
    return render(request, './main.html', context)


def car_page(request):
    context = {}
    return render(request, 'car.html', context)
