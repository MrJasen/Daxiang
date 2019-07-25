namelist = ['user4', 'user1', 'user2', 'user3', 'admin']
if namelist:
    for name in namelist:
        if name == 'admin':
            print("hello admin ")
        else:
            print("hello" + name + " thank you come here")
else:
    print("is null")
