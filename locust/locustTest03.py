#locust 参数化实现

import random
import string

from locust import HttpLocust, TaskSet, task

import os, sys

import hashlib
from hashlib import sha1
import hmac
import base64

# 定于用户行为


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

#
def md5_32(str):
    # import hashlib

    md5code = hashlib.md5(str.encode("utf-8")).hexdigest()
    return md5code


class UserBehavior(TaskSet):

    def on_start(self):
        self.baidu_index()

    def handf(self):
        a = SHA1_HMAC(appSalt, sid)

        sig = a.replace("+", "-").replace("/", "_").replace("=", "")



        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        aid = ran_str

        did = md5_32(aid)
        key = did + '12345678'
        type = '1'
        extra = 'getuser'

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

        return headers, form


    @task
    def baidu_index(self):
        headers, form = self.handf()

        self.client.post('/6/cgi/device_register', headers=headers, data=form)





class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

# os.system("locust -f locustTest02.py --host=http://xproxy.ksmobile.com")
# 直接运行
