sandwich_orders = ['a','b','c','d','e','e','e','e']
print('e没了')
while 'e' in sandwich_orders:
    sandwich_orders.remove('e')
print('现在还剩下',sandwich_orders)