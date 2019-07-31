def make_album(name, music, num=''):
    name=name.title()
    music=music.title()
    person = {'name': name, 'music': music}
    if num:
        person['num'] = num

    return person


while True:
    name = input("请输入歌手姓名，按q退出")
    if name == 'q':
        break
    music = input("请输入歌手歌曲，按q退出")
    if music == 'q':
        break
    persion = make_album(name, music)
    print(persion)
