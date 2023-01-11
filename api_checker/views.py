from django.shortcuts import render
from .api import check_api
import pandas as pd

def index(request):
    df = check_api()
    df
    return render(request, 'api_checker/api_checker.html', context)

def detail(request):
    res = check_api()
    context = {'dust': res}
    return render(request, 'api_checker/api_detail.html', context)
