users = {
    "张三":"1",
    '李四':"2",
    '王五':'4',
    '小明':'6',
    '小红':'5',
}
for key ,value in users.items():
    print(key+"\n喜欢数字"+value)

favorite_languages={
    'a':'java',
    'b':'python',
    'c':'ruby',
}
# for name , languages in favorite_languages.items():
#     print(name.title()+'的语言是'+languages.title())
#遍历字典中的所有键,默认就是遍历键，key()也是
# for name in favorite_languages:
#     print(name.title())
#遍历字典中的所有值
for lunguages in favorite_languages.values():
    print(lunguages.title())
#遍历又加判断
# friends=['b','c']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("hi  "+name.title()+",you like"+favorite_languages[name].title())
# if 'd' not in favorite_languages:
#     print("请来")