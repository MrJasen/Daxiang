import requests
import json

def token():
    url = 'http://worldcreator.ksmobile.com/v1/getToken'
    datalist={
        'dID':'b727bea5b9f26b859892cd1898e4cb33'
    }
    headers={
        'Content-Type':'application/json'
    }
    r=requests.post(url,json=datalist,headers=headers)
    json=r.json()
    return  json['result']['token']

