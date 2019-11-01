import urllib.parse
import urllib.request

# 访问的url信息（注意此处的url得是从抓包工具中获得的网址）
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

# 构造访问头信息
headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

# 构造请求数据
form_data = {
    "start": "0",
    "limit": "10",
}
data = urllib.parse.urlencode(form_data).encode('utf-8')
# 构造请求信息
request = urllib.request.Request(url, data=data, headers=headers)

json = urllib.request.urlopen(request).read().decode('utf-8')

print(json)