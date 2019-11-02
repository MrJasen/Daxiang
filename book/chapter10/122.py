# import os
# print(os.path.abspath('.'))
# #os.rename('1.py','2.py')
# x=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(x)
#
# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
import  pickle
d=dict(name='Bob', age =20, score=22)
# newd=pickle.dumps(d)
#
# print(newd)
# f=pickle.loads(newd)
# print(f)
#序列化
# f = open('dunmp.txt','wb')
# print(f)
# pickle.dump(d,f)
# #反序列化
# f=open('dunmp.txt','rb')
# d=pickle.load(f)
# print(d)

# import  sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# test()
# import platform
# print(platform.python_version())
# class Employee:
#     empCount = 0
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         Employee.empCount +=1
#     def __del__(self):
#         print('父类del')
#     def test(self):
#         print("这是父类")

class son():
    def __init__(self,sun):
        self.sun=sun
    def test(self):
        print("这是子类")
    def  __del__(self):
        print("子类del")

sun=son(123)
sun.test()
#print()
#sun.test()


a='2'
b=a.replace('2','3')
print(b)
