
import hashlib
import hmac
from hashlib import  sha1
import  base64
# a='A+q*2k^7MW'
# b='123456'
# c=hmac.new(bytes(a),bytes(b),sha1).digest().digest()
# c=base64.b64decode(c)
# print(c)

str='dasdasd'
by=b'w\xde\xb8\xe9\xde\x9d\xd7]\xde\xf3\xc7\xf8\xd3G\x1f\xd9\xcf:\xd3wz\xef\xde\xb5\xdb_Z\xd1\xce\xbak\xc6\xdd\xdb\xc7\xf7\xe1\xdd8\xf3\xafuq\xceu\xef\xa6\xb4'
m=hashlib.md5(by.encode('utf-8')).hexdigest()
print(m)