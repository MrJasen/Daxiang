# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue
#     print(n)

# name = {'aaa':100,'bbb':200,'ccc':300}
# print(name)
# name['ddd']=400
# print(name)
# name.pop('ddd')
# print(name)

# s=set([1,2,3,4])
# print(s)
# s.add(5)
# print(s)
# s.add(3)
# print(s)

# a=-100
# print(abs(a))

# n1=255
# print(hex(n1))

# def my_abs(x):
#     if x<=0:
#         return -x
#     else:
#         return x
# print(my_abs(-100))

# a=20
# print('a=',a)
l = list()    # 实例化一个 list 对象 l
l.append(1)    # 调用 l 的 append 方法
l.append(2)
l.remove(1)
print(l.__len__())    # 调用对象的 `__len__` 方法