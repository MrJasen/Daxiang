#字典中存放列表
favorite_places={
    '小豹':['北京，上海'],
    '小度':['广西，广东，深圳'],
    '小狗':['巴基斯坦'],
}
for name,citys in favorite_places.items():
    print('\n'+name.title()+'喜欢的地方是:')
    for city in  citys:
        print('\t'+city.title())