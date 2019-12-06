import base64
import hmac
import  hashlib

def hmac_sha256(did,key):
    key = key.encode('utf-8')
    did = did.encode('utf-8')
    str1 = base64.b64decode(hmac.new(key, did, digestmod=hashlib.sha256).hexdigest())
    #byte转str
    #str1=str1.decode('utf-8','ignore')
    print(str1)
    #return str1

def jiami_md5(str1):
    login_sign = hashlib.md5(str1.encode('utf-8')).hexdigest()
    return login_sign

# a=jiami_md5(hmac_sha256('0f6b98327e70dd897a1840baca953790','0f6b98327e70dd897a1840baca95379012345678'))
# print(a)
hmac_sha256('0f6b98327e70dd897a1840baca953790','0f6b98327e70dd897a1840baca95379012345678')
#print(a)