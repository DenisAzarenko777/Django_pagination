import urllib
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from app import settings
from functionCSV import  function_csv2, function_csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    next_page_url = 'write your url'


    content = function_csv() # Вызов функции которая возвращает список (list) словарей (dict)
    page_number = int(request.GET.get('page',1)) # параметр по умолчанию 1 то есть с первой страницы
    url = reverse('bus_stations') # Базовый url

    paginator = Paginator(content, settings.ITEMS_PER_PAGE) # Разбили весь контент на определенное количество записей на каждой странице
    page_obj = paginator.get_page(page_number)  # в зависимости от параметра выдает контент, который находится на этой страничке
    last_page = paginator.num_pages
    if page_obj.number != last_page:
        if page_obj.has_next():
            params = urllib.parse.urlencode({'page': page_obj.next_page_number()})
            next_page_url = f'{url}?{params}'
        else:
            next_page_url = None
    else:
        next_page_url = None
    if page_obj.has_previous():
        params2 = urllib.parse.urlencode({'page': page_obj.previous_page_number()})
        current_page = page_obj.number
        prev_page_url = f'{url}?{params2}'
    else:
        prev_page_url = None
    last_page = paginator.num_pages
    return render(request, 'index.html', context={
            'bus_stations': page_obj.object_list,
            'current_page': current_page,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url,
            'last_page': last_page,
        })

