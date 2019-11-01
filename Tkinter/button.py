# noinspection PyUnresolvedReferences
from  tkinter import  *
root=Tk()

def hellobutton():
    print('hello button')

#通过点击来执行绑定方法，打印hello
# Button(root,text='hello!!',command=hellobutton).pack()
# root.mainloop()

#加一个relief=FLAT，就跟Label一样了
# Button(root,text='hello2',relief=FLAT).pack()
# root.mainloop()

#设置button的效果
# Button(root,text='hello',relief=FLAT).pack()
# Button(root,text='hello',relief=GROOVE).pack()
# Button(root,text='hello',relief=RAISED).pack()
# Button(root,text='hello',relief=RIDGE).pack()
# Button(root,text='hello',relief=SOLID).pack()
# Button(root,text='hello',relief=SUNKEN).pack()
# root.mainloop()

#Button文本与图像,,,,,  compound是位图和文本的关系
# Button(root,text='button',compound='bottom',bitmap='error').pack()
# Button(root,text='button',compound='left',bitmap='error').pack()
# Button(root,text='button',compound='right',bitmap='error').pack()
# Button(root,text='button',compound='top',bitmap='error').pack()
# Button(root,text='button',compound='center',bitmap='error').pack()
# root.mainloop()

#使用对象来设置button的宽度和高度
# b1=Button(root,width=10,height=2,text='b1111',bg='yellow')
# b1.pack()
#
# #使用属性来设置
# b2=Button(root,text='b2222')
# b2['width']=30
# b2['height']=3
# b2['relief']=SUNKEN
# b2.pack()
#
# #使用configure方法指定
# b3=Button(root,text='b33333')
# b3.configure(width=30,height=3,bg='blue')
# b3.pack()
# root.mainloop()

#设置button文本在控件上的显示位置
#简单就是美！
# for a in ['n','s','e','w','ne','nw','se','sw']:
#     Button(root,
#     text = 'anchor',
#     anchor = a,
#     width = 30,
#     height = 4).pack()
# root.mainloop()

#设置button的前景色fg，和背景色bg
# Button(root,text='我是前景色',fg='blue').pack()
# Button(root,text='我是背景色',bg='yellow').pack()
# root.mainloop()

#button焦点
def cb1():
    print('button 1 clicked')
def cb2():
    print('button2 clicked')
def cb3():
    print('button3 clicked')

b1=Button(root,text='button1',command=cb1)
b2=Button(root,text='button2')
b2.bind('<Return>',cb2)
b1.pack()
b2.pack()
root.mainloop()
