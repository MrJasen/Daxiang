from greenlet import  greenlet
def proc1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def proc2():
    print(56)
    gr1.switch()
    print(78)

#if __name__=="__main__":
gr1=greenlet(proc1)#启动一个协程
gr2=greenlet(proc2)
gr1.switch()#先执行gr1指定运行的函数，然后再切换到gr2


