from django.shortcuts import render
from .api import check_api, create_candles
import json


# def index(request):
#     res = check_api()
#     json_ob = json.loads(res)
#     choice = json_ob["data"]["item"]
#     year = []
#     date = []
#     price = []
#     for dct in choice : 
#         year.append(dct["yyyy"])
#         date.append(dct["regday"])    
#         price.append(dct["price"])

#     context = {'year': '2022', 'price': price}
#     return render(request, 'common/api_checker.html', context)

# def detail(request):
#     res = check_api()
#     context = {'dust': res}
#     return render(request, 'common/api_detail.html', context)

# def index(request):
#     res = check_api()
#     context = {'dust': res}
#     return render(request, 'common/api_checker.html', context)

# def detail(request):
#     res = check_api()
#     context = {'dust': res}
#     return render(request, 'common/api_detail.html', context)

# 예측하는 페이지 전에 보여주는 페이지.
def index(request):
    res = check_api()
    return render(request, 'common/predict.html')

def detail(request):
    res = check_api()
    res2 = create_candles(res,)
    # res를 dict로 바꿔서 context에 넣어준다.
    context = {'res': res}
    return render(request, 'common/api_detail.html', context)


