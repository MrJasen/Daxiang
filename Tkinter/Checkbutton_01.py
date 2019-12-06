#coding=utf-8
from tkinter import  *
root=Tk()

# #第一个checkbutton
# Checkbutton(root,text='python').pack()
# root.mainloop()

# #事件处理
# def printButton():
#     print('you check this button')
# Checkbutton(root,text='check python',command=printButton).pack()
# root.mainloop()

# #改变checkbutton显示文本
# v=StringVar()
# def changeButton():
#     v.set('check tkinter')
# v.set('check python')
# Checkbutton(root,text='check python',textvariable=v,command=changeButton).pack()
# root.mainloop()

# #变量与checkbutton绑定,勾选默认值是1，没勾是0. variable是与控件绑定
# v=IntVar()
# def changeIntButton():
#     print(v.get())
# Checkbutton(root,text='check button value',variable=v,command=changeIntButton).pack()
# root.mainloop()

#修改默认值
v=StringVar()
def changeStringButton():
    print(v.get())
Checkbutton(root,text='checkbutton value',
            variable=v,command=changeStringButton,
            onvalue='python',offvalue='tkinter').pack()
root.mainloop()