#coding=utf-8
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

def hash_hmac(key, msg):
    # 先进行sha1加密
    my_sign = hmac.new(bytes(key,'utf-8'), bytes(msg,'utf-8'), sha1).digest()
    #print(my_sign)
    # base64 是编码方式，变成2进制，可逆，ecode编码，默认是bytes不能replace()，要decode指定编码格式变成str
    my_sign = base64.b64encode(my_sign).decode('utf-8')
    my_sign = my_sign.replace('+', '-').replace('/', '_').replace('=', '')
    return my_sign

def get_sig():
    sig=hash_hmac(appSalt,sid)
    return sig

def get_did():
    # 随机生成一个16位字符
    a = "".join([choice("0123456789ABCDEF") for i in range(16)])
    did = hashlib.md5(a.encode()).hexdigest()
    return did

#随机生成key
def get_key():
    # 随机生成一个16位字符
    a = "".join([choice("0123456789ABCDEF") for i in range(16)])
    md5_aid = hashlib.md5(a.encode()).hexdigest()
    key=md5_aid+'12345678'# key为40位注册密码字符串
    return  key

#参数化设备id，自动生成对应的key
def get_add_key(did):
    addkey=did+'12345678'
    return addkey

#hmac_sha256加密
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

# MD5加密获取sign
#get_md5_sign(get_hmac_sha256(key,did))
def get_md5(str):
    m = hashlib.md5()
    m.update(str.encode('UTF-8'))
    return m.hexdigest()

#二种加密方式合一获取sign
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
# a=get_sig()
# b=get_did()
# c=get_key()
# print(a)
# print(b)
# print(c)
