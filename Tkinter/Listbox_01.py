#coding=utf-8
from tkinter import  *
root=Tk()

#单选
# lb=Listbox(root)
# for item in ['a','b','c']:
#     lb.insert(END,item)
# lb.pack()
# root.mainloop()
#多选

def help():
    print("hello")
menubar=Menu(root)
# for item in ['a','b','c']:
#     menubar.add_command(label=item,command=help)
# root['menu']=menubar
# root.mainloop()
filemenu=Menu(menubar,tearoff=0)
for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_commad(label=item, command=help)
#将 menubar 的 menu 属性指定为 filemenu，即 filemenu 为 menubar 的下拉菜单
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()
