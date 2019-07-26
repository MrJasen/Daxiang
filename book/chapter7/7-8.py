sandwich_orders =['草莓味','香草味','巧克力味']
finished_sandwiches=[]
# for oders in sandwich_orders:
#     print("我给你做了",oders,"三明治")
# finished_sandwiches=sandwich_orders.pop()
# print(finished_sandwiches)
while sandwich_orders:
    temp=sandwich_orders.pop()
    finished_sandwiches.append(temp)
    print('现在有',finished_sandwiches,'口味的')
