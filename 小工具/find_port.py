
import os
def is_port_used(port, kill=False):
    cmd = 'netstat -ano | findstr {} | findstr  LISTENING'.format(port)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)
    pid = None
    if result != '':
            pid = result.split()[-1]
            result = os.popen('tasklist /FI "PID eq {0}'.format(pid)).read()  #类型是str
            print(result)
            position = result.rfind('=====')
            program_name = result[position + 5:].split()[0]
            print('当前查询的程序是',program_name)
            result = os.popen('wmic process where name="{0}" get executablepath'.format(program_name)).read()
            result = result.split()[-1]
            print('占用的程序所在位置:',result)
    elif  kill:
        if not pid:
            raise Exception("pid is None")
        print(os.popen("taskkill /F /PID {0}".format(pid)).read())  # 结束进程
    else:

        print('端口"',port,'"没有被占用')
if __name__ == '__main__':
    while(True):
        num=input('请输入要查询的端口：')
        is_port_used(num)
        input('输入回车键继续查询')

