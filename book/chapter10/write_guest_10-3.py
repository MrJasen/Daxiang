name=input("please input your name")
filename='guest.txt'
with open(filename,'a') as file_object:
    file_object.write(name+'\n')
    print('wirte sus '+name)