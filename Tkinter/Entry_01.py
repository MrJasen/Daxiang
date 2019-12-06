# coding=utf-8
from tkinter import  *
root=Tk()

#Entry不能设置text文本，不起作用
# Entry(root,text='input this here').pack()
# root.mainloop()

# Entry与变量绑定,设定初始值
# e=StringVar()
# entry=Entry(root,textvariable=e)
# e.set('input this here')
# entry.pack()
# root.mainloop()

#设置entry为只读
# e=StringVar()
# entry=Entry(root,textvariable=e,state='readonly')
# e.set('please input')
# entry.pack()
# root.mainloop()

# #设置密码,show可以指定特殊符号
# e=StringVar()
# pwd=Entry(root,textvariable=e,show='*')
# e.set('')
# pwd.pack()
# root.mainloop()

# #检验输入的内容，(无效)
# e=StringVar()
# def validateText(contents):
#     print(contents)
#     return  contents.isalnum()
#
# entry=Entry(root,validate='key',textvariable=e,validatecommand=validateText)
# entry.pack()
# root.mainloop()
