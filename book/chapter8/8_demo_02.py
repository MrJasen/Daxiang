def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]

    return magicians


magicians = ['David', 'liu', 'Bear']

make_great(magicians)
#print(magicians)
show_magicians(magicians)