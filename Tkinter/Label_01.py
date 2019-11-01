# noinspection PyUnresolvedReferences
from  tkinter import  *
root=Tk()

#创建label
# label=Label(root,text='hello')
# label.pack()
# root.mainloop()

#打印到标题
# root.title('hello')
# root.mainloop()

#使用内置位图(内置托图片)
# lable=Label(root,bitmap='gray75')
# lable.pack()
# lable.mainloop()

#改变lable的前景色和背景色
# Label(root,fg='blue',bg='yellow',text='刘然牛批 ').pack()
# root.mainloop()

#创建三个label，长度跟文字长度有关
# Label(root,bg='red',text='red').pack()
# Label(root,bg='blue',text='blue').pack()
# Label(root,bg='yellow',text='yellow').pack()
# root.mainloop()

#创建三个lable，给长度和高度加上限制
# Label(root,bg='blue',width=10,height=3,text='blue').pack()
# Label(root,bg='red',width=10,height=3,text='red').pack()
# Label(root,bg='yellow',width=10,height=3,text='yellow').pack()
# root.mainloop()

#compound文本与图像在label上的显示,(位图小图标和文字的关系)
# label=Label(root,text='error',compound='left',bitmap='error')
# label.pack()
# label.mainloop()

#建立一个text长文本，看看如何显示的
# label=Label(root,text='welcome to China HaHa welcome to China HaHa!',width=20,height=3,bg='yellow') #发现超过控件的部分被截断了
# label.pack()
# label.mainloop()

#左对齐，文本居中
# label=Label(root,
#       text='welcome to jcodeer,cublog,cn',
#       bg='yellow',
#       width=10,
#       height=3,
#       wraplength=80,
#       justify='left')
# label.pack()
# label.mainloop()

#居中对齐，文本居左
Label(root,
text = 'welcome to jcodeer.cublog.cn',
        bg = 'red',
        width = 40,
        height = 3,
        wraplength = 80,
        anchor = 'w'
        ).pack()

#居中对齐，文本居右
Label(root,
        text = 'welcome to jcodeer.cublog.cn',
        bg = 'blue',
        width = 40,
        height = 3,
        wraplength = 80,
        anchor = 'e'
        ).pack()
root.mainloop()
