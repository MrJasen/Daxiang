def make_album(name, music, num=''):
    person = {'name': name, 'music': music}
    if num:
        person['num'] = num
    return person


person1 = make_album('jay', '七里香')
print(person1)
person2 = make_album('jj', '江南')
print(person2)
person3 = make_album('ljs', 'nb', '666')
print(person3)
