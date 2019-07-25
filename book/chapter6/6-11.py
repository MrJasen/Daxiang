cities = {
    '北京':{
        '国家':'中国',
        '人口':"1000w",
        '简介':'老城市',
    },
    '上海':{
        '国家':'中国',
        '人口':"500w",
        '简介':'大城市',
    },
    '南昌':{
        '国家':'中国',
        '人口':"10w",
        '简介':'小城市',
    },
}
for name,city_info in cities.items():
    print("城市名："+name.title())
    guojia=city_info['国家']
    renkou=city_info['人口']
    jianjie=city_info['简介']
    print('\t国家是：'+guojia.title())
    print('\t人口是：',renkou.title())
    print('\t简介是: ',jianjie.title())