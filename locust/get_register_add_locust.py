# noinspection PyUnresolvedReferences
from random import *
from hashlib import sha1
import base64
import hmac
import requests
import hashlib
from locust import HttpLocust, TaskSet, task
appSalt = 'A+q*2k^7MW'
android_id = '0265b60e6754c2e4'
sid = '123456'
appid = '175309054'

# sig签名生成
def hash_hmac(key, msg):
    # 先进行sha1加密
    my_sign = hmac.new(bytes(key, 'utf-8'), bytes(msg, 'utf-8'), sha1).digest()
    # base64 ecode
    my_sign = base64.b64encode(my_sign).decode('utf-8')
    # 处理url
    my_sign = my_sign.replace('+', '-').replace('/', '_').replace('=', '')
    return my_sign


# sid生成
def new_sid(aid):
    md5_aid = hashlib.md5(aid.encode()).hexdigest()
    return md5_aid


# 构造注册
def get_register():
    # 随机生成一个16位字符
    did = "".join([choice("0123456789ABCDEF") for i in range(16)])
    key = new_sid(did+'12345678')  # key为40位注册密码字符串
    sig = hash_hmac(sid, appSalt)
    type = '1'
    extra = 'getuser'

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
    r = requests.post(url, json=payload, headers=headers)
    print(r.json())


get_register()
class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000