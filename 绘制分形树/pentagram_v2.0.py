'''
    作者：刘佳顺
    功能：五角星绘制
    版本：1.0
    日期：2019年3月12日12:59:17
'''
import turtle
def draw(size):
    while size <= 100:
        count = 1
        while count <= 5:
            turtle.forward(size)
            turtle.right(144)
            count = count + 1
        size = size + 10


def main():
    '''
    主函数
    '''
draw(50)

if __name__== '__main__':
    main()


#111
#222s
