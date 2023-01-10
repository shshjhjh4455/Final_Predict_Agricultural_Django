import requests
import json
import pprint
from urllib.parse import urlencode, unquote, quote_plus
from bs4 import BeautifulSoup


serviceKey = "c51eace9-59a8-4c45-921f-ad68c3507a7b"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

"""sample = http://www.kamis.or.kr/service/price/json.do?action=periodProductList&p_productclscode=02&p_startday=2015-10-01
    &p_endday=2015-12-01&p_itemcategorycode=200&p_itemcode=212&p_kindcode=00&p_productrankcode=04&p_countrycode=1101
    &p_convert_kg_yn=Y&p_cert_key=111&p_cert_id=222&p_returntype=xml"""



# def check_api():
#     itemname = []
#     price = []
#     url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList"
#     p_productclscode="02"
#     p_startday="2022-01-20"
#     p_endday="2023-01-05"
#     p_itemcategorycode="200"
#     p_itemcode="211"
#     p_kindcode="00"
#     p_productrankcode="04"
#     p_countrycode="default"
#     p_convert_kg_yn="default"


    # queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('p_productclscode') : p_productclscode, quote_plus('p_startday') : p_startday, quote_plus('p_endday') : p_endday, quote_plus('p_itemcategorycode') : p_itemcategorycode, quote_plus('p_itemcode') : p_itemcode, quote_plus('p_kindcode') : p_kindcode, quote_plus('p_productrankcode') : p_productrankcode, quote_plus('p_countrycode') : p_countrycode, quote_plus('p_convert_kg_yn') : p_convert_kg_yn })
    # res = requests.get(url + queryParams)
    # xml = res.text
    # soup = BeautifulSoup(xml, 'html.parser')
    # for tag in soup.find_all('itemname'):
    #     itemname.append(tag.text)
    # for tag in soup.find_all('price'):
    #     price.append(tag.text)
    # res = dict(zip(itemname, price))
    # return res

def check_api():
    itemname = []
    price = []
    url = "http://www.kamis.or.kr/service/price/xml.do?action=periodProductList"
    returnType="json"
    ID = 3067
    p_itemcategorycode = 200
    p_itemcode = 211
    start_date = "2022-01-01"
    end_date = "2023-01-10"

    queryParams = '?' + urlencode({ 
                                   quote_plus("p_startday") : start_date, 
                                   quote_plus("p_endday") : end_date,
                                   quote_plus("p_itemcategorycode") : p_itemcategorycode, 
                                   quote_plus("p_itemcode") : p_itemcode, 
                                   quote_plus('p_cert_key') : serviceKeyDecoded, 
                                   quote_plus('p_cert_id') : ID, quote_plus('p_returntype') : returnType })


    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('itemname'):
        itemname.append(tag.text)
    for tag in soup.find_all('price'):
        price.append(tag.text)
    res = dict(zip(itemname, price))
    return res