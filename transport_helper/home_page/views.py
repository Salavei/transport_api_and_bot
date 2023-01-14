from django.http import JsonResponse
from django.shortcuts import render
from home_page.utils.business_logic import parse_money


def pants_page(request):
    context = {**parse_money()[0], **parse_money()[1]}
    return render(request, 'main.html', context=context)


def api_course_page(request):
    exchange_money_dict = parse_money()[0]
    average_salary = parse_money()[1]
    context = {'exchange_money': exchange_money_dict, 'average_salary': average_salary}
    return JsonResponse(context)
