Destination =['lijiang','xizang','chengdu','beijing','lasa']
#原始打印
print(Destination)
#使用sorted()临时排序，按照英文顺序升序
print(sorted(Destination))
#再次打印，实际顺序未改变
print(Destination)
#使用sorted()临时排序，按照字母相反顺序打印，也是不要改变
print(sorted(Destination,reverse=True))
#再次打印，证明顺序没变
print(Destination)
#使用reverse()修改顺序，使顺序改变
Destination.reverse()
print(Destination)
#恢复成原来样子
Destination.reverse()
print(Destination)
#使用sort()方法，使列表永久按照字幕排序
Destination.sort()
print(Destination)
#使用sort()的reverse，使顺序倒序
Destination.sort(reverse=True)
print(Destination)
#看看有多少个元素
print(len(Destination))
print(Destination[4])
