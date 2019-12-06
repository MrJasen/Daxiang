# noinspection PyUnresolvedReferences
from random import *
from hashlib import sha1
import base64
import hmac
import requests
import hashlib
import  json
import unittest

appSalt = 'A+q*2k^7MW'
android_id = '0265b60e6754c2e4'
sid = '123456'
appid = '175309054'

# sig签名生成
def hash_hmac(key, msg):
    # 先进行sha1加密
    my_sign = hmac.new(bytes(key,'utf-8'), bytes(msg,'utf-8'), sha1).digest()
    print(my_sign)
    # base64 是编码方式，变成2进制，可逆，ecode编码，默认是bytes不能replace()，要decode指定编码格式变成str
    my_sign = base64.b64encode(my_sign).decode('utf-8')
    # print(my_sign)
    # my_sign=base64.b64decode(my_sign)
    # print(my_sign)
    # 处理url
    my_sign = my_sign.replace('+', '-').replace('/', '_').replace('=', '')
    return my_sign


# sid生成
def new_sid(aid):
    md5_aid = hashlib.md5(aid.encode()).hexdigest()
    return md5_aid

#hmac-sha256加密
def hmac_sha256(did,key):
    key = key.encode('utf-8')
    did = did.encode('utf-8')
    str1 = base64.b64decode(hmac.new(key, did, digestmod=hashlib.sha256).hexdigest())
    #byte转str
    str1=str1.decode('utf-8','ignore')
    return str1

#获取登陆签名
def get_loginSign(str1):
    login_sign = hashlib.md5(str1.encode('utf-8')).hexdigest()
    return login_sign

#构造注册
def get_register():
    # 随机生成一个16位字符
    a = "".join([choice("0123456789ABCDEF") for i in range(16)])
    did = new_sid(a)
    print('did====',did)
    key=did+'12345678'# key为40位注册密码字符串

    sig = hash_hmac(appSalt,sid)
    print('sig====',sig)
    type = '1'
    extra = 'getuser'
    print('key====',key)
    print('did===',did)
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'sig': sig,
               'appid': appid,
               'sid': sid
               }
    payload = {'did': did,
               'key': key,
               'type': type,
               'extra': extra
               }
    url = 'http://xproxy.ksmobile.com/6/cgi/device_register'
    r = requests.post(url, data=payload, headers=headers)
    json_string=r.json()
    #print(json_string)

    # print(r.content.decode("utf-8"))
    # print(r.text)
    a=r.content.decode("utf-8")
    print(a)

    # ret=json.dumps(json_string['ret'])
    # print(ret)

#登陆
    # sign = get_loginSign(hmac_sha256(did, key))
    # print('sign====',sign)
    # payload2 = {'did': did,
    #           'sign':sign,
    #            'type': type,
    #            'extra': extra
    #            }
    # url2 = 'http://xproxy.ksmobile.com/6/cgi/device_login'
    # r = requests.post(url2, data=payload2, headers=headers)
    # json_string = r.json()
    # print(json_string)
#发验证码



#发送验证码
def send_code():
    pass


#登陆
def login():
    # 随机生成一个16位字符
    a = "".join([choice("0123456789ABCDEF") for i in range(16)])
    did = new_sid(a)
    key = did + '12345678'  # key为40位注册密码字符串
    sig = hash_hmac(appSalt, sid)

    type = '1'
    extra = 'getuser'

    sign=get_loginSign(hmac_sha256(did,key))
    print('key====', key)
    print('did===', did)
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'sig': sig,
               'appid': appid,
               'sid': sid
               }
    payload = {'did': did,
              'sign':sign,
               'type': type,
               'extra': extra
               }
    url = 'http://xproxy.ksmobile.com/6/cgi/device_login'
    r = requests.post(url, data=payload, headers=headers)
    json_string = r.json()
    print(json_string)


# class login(unittest.TestCase):
#     def setUp(self):
#         self.base_url='http://xproxy.ksmobile.com/version/cgi/device_login'
#     def test_get_sucess(self):
#         datalist={'did':'265354e3370b10b1000000005dafd13d',
#                   'sign':sign}
#         headers={'Content-Type': 'application/x-www-form-urlencoded',
#                  'sid':sid,
#                  'sig':'265354e3370b10b1000000005dafd13d',
#                  'appid':appid
#                  }

get_register()
#login()



