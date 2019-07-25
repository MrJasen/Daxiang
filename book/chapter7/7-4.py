pormpt = '请输入一个披萨配料,输入quit退出'
message = ''

while message != 'quit':
    message = input(pormpt)
    if message != 'quit':
        print('我们会在配料中加入' + message + '\n')
