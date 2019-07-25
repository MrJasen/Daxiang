# 序数：
# 在一个列表中存储数字1~9
# 遍历这个列表
# 循环使用一个if-elif-else结构，打印每个数字对应的序数，输出内容为
# 1st、2nd、3rd、4th、5th、6th、7th、8th、9th，每个序数独占一行
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(number, "st")
    elif number == 2:
        print(number, "nd")
    elif number == 3:
        print(number, "rd")
    else:
        print(number, "th")
