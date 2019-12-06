#coding=utf-8
import requests,json

url='http://www.baidu.com'
r=requests.get(url)
print(r.json())
