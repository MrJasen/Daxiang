#检查两个字符串相等或不等
string1 = 'a'
print(string1 == 'a')
print(string1 == 'A')
#lower()转小写函数来比较
print(string1.lower()=='a')
#比较数字
a = 10
b = 10
#print(a==b)
print(a > 1 and b<20)
print(a>100 or  b<100)
#测试特定的值是否在某一列表中
list = [1,2,3,4,5]
print('1在list里',1 in list)
print('6不在list里',6 not in list)

age = 19
if age >=18:
    print("可参加")