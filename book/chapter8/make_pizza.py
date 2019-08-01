#直接导入，然后模块名点函数名调用
#import pizaa
#pizaa.make_pizza(20,'aaa','bbb')

#从模块中导入想要的函数
# from  pizaa import make_pizza
# make_pizza(20,'222','333')

#从模块中导入函数名，然后给函数起一个别名
# from pizaa import  make_pizza as mp
# mp(30,22,55,55)

#直接导入模块，然后给模块起别名
# import pizaa as pz
# pz.make_pizza(22,44,55,33)

#从模块中引入所有函数
from  pizaa import  *
make_pizza(44,44,55,66)
