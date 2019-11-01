# freshfruit = ['bana  na', 'loganbe  rry ', '      pas  sion f  ruit                    ']
# aa=[weapon.strip()   for weapon in freshfruit]
# print(aa)

# vec = [ 2,4,6]
# a=[3*x for x in vec if x>3]
# print(a)
ver1 = [2,3,6]
ver2 = [3,-4,-5]
print([x*y for x in ver1 for y in ver2])
print([x+y for x in ver1 for y in ver2])
print([ver1[i]*ver2[i] for i in range(len(ver1))])