#coding=utf-8
import  json

# d=dict(name='bob',age=20,score=30)
# json.dumps(d)
# print(json.dumps(d))
# print(type(json.dumps(d)))

# 反序列化
# json_str='{"age": 20, "score": 88, "name": "Bob"}'
# a=json.loads(json_str)
# print(a)
obj=dict(name='小明',age=20)
v=json.dumps(obj)
s=json.dumps(obj,ensure_ascii=True)
print(v)
print(s)
