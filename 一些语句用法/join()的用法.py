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

# ǰ��Ĵ�����ʲô���ָ���Ȼ������һ���µ��ַ���
print(' '.join(list_of_strings))
print(type(' '.join(list_of_strings)))

# Output
# My,name,is,Chaitanya,Baweja