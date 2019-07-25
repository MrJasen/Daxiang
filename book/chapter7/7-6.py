#更新7-6三个出口
#1.标志测试来终止循环
prompt = '请输入年龄，我告诉你票价，按quit退出'
active = True
while active:
    message = input(prompt)
    #print(type(message))
    if message == 'quit':
        print('已退出')
        #active = False
        break
        #print(type(message))
    # else:
    #         print("输入有误，请输入数字或者quit")
    message = int(message)
    if message < 3:
        print('免费')
    elif message < 12:
        print('10$')
    else:
        print('15$')