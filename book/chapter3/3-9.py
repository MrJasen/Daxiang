#学习遍历列表
magic=['sb1','sb2','sb3']
#使用for循环遍历list、
    print(magic)
for people in magic:
    #使用临时变量的title()方法打印抬头
    print(people.title()+" 真牛逼啊！")
    #期待他的下一次表演,加入换行
    print('你真牛逼，下次再来!：'+ people.title() +'\n')
print('大家都是最棒的！下次见')