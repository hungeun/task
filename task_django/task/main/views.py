from http.client import HTTPResponse
from unittest import result
from django.shortcuts import render
import folium # pip install folium

import csv
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup





def task_csv(request):
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    queryParams = '?' + \
              'ServiceKey=' + 'NRK%2FUglSq%2FFDnatZ9nBXDaI0HX0fQO07XIMNZUq4cxm02TKntPlUa%2Bx5DaQdUl0PPaBW9ZOpEaNlzztBm%2BGIzA%3D%3D'+ \
              '&pageNo='+ '1' + \
              '&numOfRows='+ '999' + \
              '&dataType='+ 'JSON' + \
              '&dataCd='+ 'ASOS' + \
              '&dateCd='+ 'DAY' + \
              '&startDt='+ '20180601' + \
              '&endDt='+ '20200421' + \
              '&stnIds='+ '108' # \ 뒤에 공백 금지

    result = requests.get(url + queryParams)
    js = json.loads(result.content)
    data = pd.DataFrame(js['response']['body']['items']['item'])

    li = ['stnId','tm','avgTa','minTa','maxTa','sumRn','maxWs','avgWs','ddMes']

    html = data.loc[:,li]
    return render(request, 'task.html', {'html':html})
    # data = pd.read_csv('C:/Users/hungeun/Downloads/task_django/task/task.csv')
    # context = {'df' : data.to_html() } 
    #     # index=False, justify='center'
    # return render(request,'task.html', context)

def map_(request):
    map = folium.Map(location=[36.34, 127.77],width='100%',height='100%',zoom_start=6.4)

    #서울특별시
    folium.Circle(radius=50, location=[37.5711, 126.9827], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[37.5711, 126.9827], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)

    #인천광역시
    folium.Circle(radius=50, location=[37.4533, 126.7108], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[37.4533, 126.7108], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)

    #대전광역시
    folium.Circle(radius=50, location=[36.3364, 127.3920], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[36.3364, 127.3920], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)

    #광주광역시
    folium.Circle(radius=50, location=[35.16, 126.85], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[35.16, 126.85], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)
    
    #부산광역시
    folium.Circle(radius=50, location=[35.1639, 129.0674], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[35.1639, 129.0674], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)
    
    #울산광역시
    folium.Circle(radius=50, location=[35.5318, 129.3146], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[35.5318, 129.3146], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)

    #제주특별시
    folium.Circle(radius=50, location=[33.3606, 126.5405], popup='Sewoon Sangga', color='#3186cc', fill=True, fill_color='#3186cc').add_to(map)
    folium.CircleMarker(location=[33.3606, 126.5405], radius=10, popup='Makercity Sewoon', color='crimson', fill=False).add_to(map)

    map.add_child(folium.LatLngPopup())
    maps = map._repr_html_()
    return render(request,'task.html',{'map':maps})

def task(request):
    return render(request,'task.html')