prompt = '请输入年龄，我告诉你票价，按0退出'
active = True
while active:
    message = input(prompt)
    print(type(message))
    # if type(message)!=int:
    #        break
    #        #active=False
    #else:
    message = int(message)
    if message == 0:
        print('已退出')
        active = False
        #print(type(message))
    elif message < 3:
        print('免费')
    elif message < 12:
        print('10$')
    else:
        print('15$')



