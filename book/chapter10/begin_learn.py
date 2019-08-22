print('--------------读取整个文件--------------')
with open('learning_python.txt',encoding='utf-8') as file_object:
    contens= file_object.read()
    print(contens)

print('--------------遍历文件对象-------------')
with open('learning_python.txt',encoding='utf-8') as file_object:
    for line in file_object:
        print(line.rstrip())

print('------------存储成列表在外面打印-------')
with open('learning_python.txt',encoding='utf-8') as file_object:
    lines=file_object.readlines()
# in_str=''
# for line in lines:
#     in_str=in_str+line
# print(in_str)
for line in lines:
    print(line.rstrip())