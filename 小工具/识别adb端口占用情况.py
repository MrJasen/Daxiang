
import os
def is_port_used(port=5037, kill=False):
    cmd = 'netstat -ano | findstr {} | findstr  LISTENING'.format(port)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)
    pid = None
    if result != '':
        try:
            pid = result.split()[-1]
            result = os.popen('tasklist /FI "PID eq {0}'.format(pid)).read()
            """:type: str """
            print(result)
            position = result.rfind('=====')
            program_name = result[position + 5:].split()[0]
            print("占用的程序是{}".format(program_name))
            result = os.popen('wmic process where name="{0}" get executablepath'.format(program_name)).read()
            result = result.split()
            print("占用的程序所在位置：{}".format(result[1]))
            cmd = "explorer {0}".format(os.path.dirname(result[1]))
            print('123123',cmd)
            os.chdir(r'')
            #s.chdir(cmd)
            #execute_cmd(cmd)  # 打开所在文件夹
        except Exception:
            import traceback
            traceback.print_exc()
        finally:
            if kill:
                if not pid:
                    raise Exception("pid is None")
                print(os.popen("taskkill /F /PID {0}".format(pid)).read())   # 结束进程
    else:
        print('{}端口没有被占用'.format(port))
if __name__ == '__main__':
    is_port_used()
    input()