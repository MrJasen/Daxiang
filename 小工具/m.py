# noinspection PyUnresolvedReferences
import time,os,sys
from tkinter import  *



# now=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
# print(now)
# path=os.path.dirname(os.path.abspath(sys.argv[0]))
# print(path)
def get_status():
    cmd1='adb get-state'
    str=os.popen(cmd1).read().split()[0]
    return str

def show():
    status = get_status()
    if status == 'device':
        root=Tk()
        li = ['C', 'python', 'php', 'html', 'SQL', 'java']
        movie = ['CSS', 'jQuery', 'Bootstrap']
        listb = Listbox(root)  # 创建两个列表组件
        listb2 = Listbox(root)
        for item in li:  # 第一个小部件插入数据
            listb.insert(0, item)

        for item in movie:  # 第二个小部件插入数据
            listb2.insert(0, item)

        listb.pack()  # 将小部件放置到主窗口中
        listb2.pack()
        root.mainloop()
    else:
        print(2)
#get_status()
show()


