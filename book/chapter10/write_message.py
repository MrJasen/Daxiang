file = 'wait_write.txt'
with open(file,'a',encoding='utf-8') as file_object:
    file_object.write("hello \n")
    file_object.write('hello2 \n')
    file_object.write("实参编程a，编程附加模式，添加这一行")