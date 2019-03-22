'''
    作者：刘佳顺
    功能：五角星绘制
    版本：1.0
    日期：2019年3月12日12:59:17
'''
import turtle

def main():
    '''
    主函数
    '''

count = 1
while count<=5:
    turtle.forward(200)
    turtle.right(144)
    count=count+1


if __name__== '__main__':
    main()