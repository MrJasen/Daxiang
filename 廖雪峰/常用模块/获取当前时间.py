#coding=utf-8
from datetime import  datetime
now=datetime.now()
print(now)
print(type(now))

#构造日期
dt=datetime(2018,5,22,22,22)
print(dt)
#把日期转为timestamp
tm=dt.timestamp()
print(tm)
#timestamp转日期
dt1=datetime.fromtimestamp(tm)
print(dt1)
