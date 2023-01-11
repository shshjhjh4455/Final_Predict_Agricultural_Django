import requests
import json
import pprint
from urllib.parse import urlencode, unquote, quote_plus
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import datetime



serviceKey = "c51eace9-59a8-4c45-921f-ad68c3507a7b"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

"""sample = http://www.kamis.or.kr/service/price/json.do?action=periodProductList&p_productclscode=02&p_startday=2015-10-01
    &p_endday=2015-12-01&p_itemcategorycode=200&p_itemcode=212&p_kindcode=00&p_productrankcode=04&p_countrycode=1101
    &p_convert_kg_yn=Y&p_cert_key=111&p_cert_id=222&p_returntype=xml"""

def check_api():
    url = "http://www.kamis.or.kr/service/price/xml.do"
    returnType="json"
    ID = 3067
    p_itemcategorycode = 200
    p_itemcode = 211
    today= datetime.datetime.today()
    start_date = (today - datetime.timedelta(365)).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    p_productrankcodes = ["04", "05"]
    
    for rank in p_productrankcodes :
    
        queryParams = '?' + urlencode({ quote_plus("action") : "periodProductList",
                                       quote_plus("p_startday") : start_date, 
                                       quote_plus("p_endday") : end_date,
                                       quote_plus("p_itemcategorycode") : p_itemcategorycode, 
                                       quote_plus("p_itemcode") : p_itemcode, 
                                       quote_plus("p_productrankcode") : rank, 
                                       quote_plus('p_cert_key') : serviceKeyDecoded, 
                                       quote_plus('p_cert_id') : ID, quote_plus('p_returntype') : returnType })
        res = requests.get(url + queryParams)

        contents = res.text
        json_ob = json.loads(contents)
        choice = json_ob["data"]["item"]

        year = []
        date = []
        price = []
        for dct in choice : 
            if dct["countyname"] == "평균" : 
                year.append(dct["yyyy"])
                date.append(dct["regday"])    
                price.append(dct["price"])

        globals()["df_"+rank] = pd.DataFrame(zip(year,date,price))
        globals()["df_"+rank].columns = ["year", "date", "price_"+rank]
        
    df = pd.merge(df_04, df_05, on = ["year","date"], how="inner")
    df["price_04"] = df["price_04"].str.replace(",","").astype("int")
    df["price_05"] = df["price_05"].str.replace(",","").astype("int")

    df["가격"] = df[["price_04", "price_05"]].mean(axis="columns").astype("int")
    df.drop(columns=["price_04", "price_05"], inplace=True)
    
    cols = ['year', 'date']
    df['날짜'] =df[cols].apply(lambda row: '/'.join(row.values.astype(str)), axis=1)
    df['날짜']= pd.to_datetime(df['날짜'])
    df= df.drop(labels=['year', 'date'], axis=1)
    
    df= df.set_index('날짜')
    
    return df

def create_candles(df, group_sizes):
    candles = {}
    for group_size in group_sizes:
        candle_df = pd.DataFrame(columns=['시가', '고가', '저가', '종가', '일자'])
        for i in range(len(df)-group_size):
            temp = df.iloc[i:i+group_size+1]
            open_price = temp.iloc[0]['가격']
            high_price = temp['가격'].max()
            low_price = temp['가격'].min()
            close_price = temp.iloc[-1]['가격']
            date = temp.iloc[-1].name
            candle_df = candle_df.append({'시가': open_price, '고가': high_price, '저가': low_price, '종가': close_price, '일자': date}, ignore_index=True)
        candles[group_size] = candle_df
    
    for key, df in candles.items():
        for group_size in group_sizes:
            if key == group_size:
                df[str(key) + '종가_shift'] = df['종가'].shift(-key)
        
    for df in candles.values():
        df.set_index('일자', inplace=True)
        df.dropna(inplace=True)
   
    return candles


def get_candle_df():
    candles = create_candles(check_api(), [5, 10, 20, 60, 120])
    candle_df_5, candle_df_10, candle_df_20, candle_df_60, candle_df_120 = (candles[size] for size in [5, 10, 20, 60, 120])

    candle_df_lasts = {key: df.iloc[-1] for key, df in candles.items()}

    for df in candle_df_lasts.values():
        df = df.T.dropna()

    return candle_df_lasts