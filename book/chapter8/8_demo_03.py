# def add(c):
#     return  'grat'+c
#
#
# l = ['1', '2', '3']
#
# d3 = [add(c) for c in l]
#
# print('d3=', d3)

a = ['1', '2', '3']
def y3(x):
    return x + 'ww'


l = list(map(y3, a))

print(l)
