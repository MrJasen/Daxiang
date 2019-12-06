from take_token import *

def login(token):
    url='http://worldcreator.ksmobile.com/v1/login'
    datalist={
        'bID':'net.lionbird.google.countryCreatorUS',
        'token':token
    }
    headers={
        'headers':'Application/json'
    }
    r=requests.post(url,json=datalist,headers=headers)
    print(r.headers['content-type'])

login(token())
