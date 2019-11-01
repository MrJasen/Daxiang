import  urllib.request
import  urllib.parse
import  urllib.error



####post
keywd="python"
keywd=urllib.request.quote(keywd)
url="http://www.baidu.com/s"
mydata=urllib.parse.urlencode({"wd":"python"}).encode('utf-8')
req=urllib.request.Request(url,mydata)
data=urllib.request.urlopen(req).read().decode("utf-8")
print(data)
