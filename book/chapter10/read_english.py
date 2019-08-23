#Plan A
filename='english.txt'
with open(filename,'r+',encoding='utf-8') as file_object:
    lines=file_object.readlines()
    #print(lines)
fp=open(filename,'w')
for line in lines:
    fp.write(line.replace('A', 'a'))
#Plan B
# filename='english.txt'
# lines = open(filename).readlines()
# fp = open(filename,'w')
# for s in lines:
#     fp.write(s.replace('A','a'))
# fp.close()



