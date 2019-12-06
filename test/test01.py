#coding=utf-8
import  os
import  hashlib
import base64
import hmac
import urllib
import binascii


did="0f6b98327e70dd897a1840baca953790"
key='0f6b98327e70dd897a1840baca95379012345678'


def get_hmac_sha256(key,did):
    # hmac_sha256加密
    signature = hmac.new(bytes(key, encoding='utf-8'), bytes(did, encoding='utf-8'), digestmod=hashlib.sha256).digest()
    # print(signature)
    # 二进制转为HEX
    HEX = signature.hex()
    # print(HEX)
    # 将字符串换为小写
    sha_256 = HEX.lower()
    return sha_256


# MD5加密
def get_md5_sign(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()



# a=get_hmac_sha256(key,did)
# print(a)
b=get_md5_sign(get_hmac_sha256(key,did))
print(b)

def get_sign(key,did):
    # hmac_sha256加密
    signature = hmac.new(bytes(key, encoding='utf-8'), bytes(did, encoding='utf-8'), digestmod=hashlib.sha256).digest()
    # print(signature)
    # 二进制转为HEX
    HEX = signature.hex()
    # print(HEX)
    # 将字符串换为小写
    sha_256 = HEX.lower()
    m = hashlib.md5()
    m.update(sha_256.encode('UTF-8'))
    return m.hexdigest()

b=get_sign(key,did)
print(b)

def get_add_key(aid):
    addkey=aid+'12345678'
    return addkey

a=get_add_key('13123')
print(a)