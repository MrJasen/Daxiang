filename='guest_book.txt'
while True:
    name=input('please input your name,or b to break')
    if name!='b':
        with open(filename,'a',encoding='utf-8') as file_object:
            print(name + " is sus write!")
            file_object.write(name+'\n')
    else:
        print("quit sus")
        break
