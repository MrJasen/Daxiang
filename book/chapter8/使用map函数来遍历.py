magics = ['AA', 'jay', 'JJ']
#xiugai=[]
def show_magicians(names):
    for magic in names:
        print(magic)

def make_great(names):
    return  "the great "+names

yes=list(map(make_great,magics))
#print(yes)

show_magicians(yes)