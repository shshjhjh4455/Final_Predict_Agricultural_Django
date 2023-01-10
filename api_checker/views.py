from django.shortcuts import render
from .api import check_api

def index(request):
    res = check_api()
    price = res.get('배추')
    context = {'itemname': '배추', 'price': price}
    return render(request, 'common/api_checker.html', context)

def detail(request):
    res = check_api()
    context = {'dust': res}
    return render(request, 'common/api_detail.html', context)