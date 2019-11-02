# def fun():
#     for i in range(20):
#         x=yield i
#         print('good',x)
#
# if __name__ == '__main__':
#     a=fun()
#     a.__next__()
#     x=a.send(5)
# print(x)
list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# 前面的代表用什么来分隔，然后会组成一个新的字符串
print(' '.join(list_of_strings))
print(type(' '.join(list_of_strings)))

# Output
# My,name,is,Chaitanya,Baweja