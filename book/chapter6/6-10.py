users = {
    "张三":["1",'11','22'],
    '李四':["2",'22','222'],
    '王五':['4','44'],
    '小明':['6'],
    '小红':['5','55','555','5555'],
}
for name,numbers in users.items():
    print("\n"+name.title()+'喜欢的数字是:')
    for num in numbers:
        print(num,end=' ')