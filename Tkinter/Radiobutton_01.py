#coding=utf-8
from tkinter import *
root=Tk()

# #设置一个单选按钮
# Radiobutton(root,text='test').pack()
# root.mainloop()

# #指定组
# v=IntVar()
# v.set()
# for i in range(3):
#     Radiobutton(root,variable=v,text='python',value=i).pack()
# root.mainloop()
#
# Radiobutton(root,text='test',value=1).pack()
# root.mainloop()

#创建两个组
listA=IntVar()
listB=StringVar()
listA.set(1)
listB.set(2)
for v in [listA,listB]:
    for i in range(3):
        Radiobutton(variable=v,value=i,text='python'+str(i)).pack()
root.mainloop()
