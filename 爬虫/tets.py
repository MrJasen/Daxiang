# coner=1
# # sum=0
# # n=100
# # while coner<=n:
# #     sum=coner+sum
# #     coner=coner+1
# # print(sum)
# count = 0
# while count<5:
#     print(count,'小于5')
#     count=count+1
# else:
#     print(count,'大于5')
import requests
import  json
url = "http://worldcreator.ksmobile.com/v1/getToken"
headers = {'content-type': 'application/json'}
requestData = {"dID": "b727bea5b9f26b859892cd1898e4cb33"}
ret = requests.post(url,json=requestData,headers=headers)
if ret.status_code == 200:
    text = json.loads(ret.text)
    print(text)
