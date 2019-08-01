magics = ['AA', 'jay', 'JJ']


# xiugai=[]
def show_magicians(names):
    for magic in names:
        print(magic)


def make_great(names):
    newlist = []
    for name in names:
        temp = 'the great '
        newname = temp + name
        newlist.append(newname)
        # print(newlist)
    return newlist


new = make_great(magics)
#print(new)
print(magics)
show_magicians(new)
# print(magics)
