import hashlib
from hashlib import sha1
import hmac
import base64

appSalt = 'A+q*2k^7MW'

sid = '123456'

appid = '175309054'


def SHA1_HMAC(key, message):
    key = bytes(key, 'utf-8')

    message = bytes(message, 'utf-8')

    my_sign = hmac.new(key, message, sha1).digest()
    # hash.digest()
    # 返回摘要，作为二进制数据字符串值
    #
    # hash.hexdigest()
    # 返回摘要，作为十六进制数据字符串值
    hashBytes = base64.b64encode(my_sign).decode('utf-8')  # 数据类型为str
    # hashBytes = base64.b64encode(my_sign)  # 数据类型为 bytes

    return hashBytes


a = SHA1_HMAC(appSalt, sid)

# print('a=',a)

sig = a.replace("+", "-").replace("/", "_").replace("=", "")

# print('sig=',sig)


aid = 'c264df2ea307bf0a'


def md5_32(str):
    # import hashlib

    md5code = hashlib.md5(str.encode("utf-8")).hexdigest()
    return md5code


did = md5_32(aid)
key = did + '12345678'
type = '1'
extra = 'getuser'

import requests

# /add


url = 'http://xproxy.ksmobile.com/6/cgi/device_register'

headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'sig': sig,
           'appid': appid,
           'sid': sid
           }
form = {'did': did,
        'key': key,
        'type': type,
        'extra': extra
        }

r = requests.post(url=url, headers=headers, data=form)

rejson = r.text

print('body1', rejson)
print("did=",key)