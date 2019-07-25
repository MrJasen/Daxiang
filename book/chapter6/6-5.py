rivers={
    'nile':'egypt',
    'songhj':'hjs',
    'huanghe':'china',
    'mxxbh':'yulin',
}
for river,guojia in rivers.items():
    print("the "+river+" runs througt "+ guojia)
#打印河流名字
for river in rivers.keys():
    print(river)
#打印国家名字
for guojia in rivers.values():
    print(guojia)