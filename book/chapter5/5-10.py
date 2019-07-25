current_users = ['a', 'b', 'c', 'd', 'e']
new_users = ['f', 'g', 'h', 'a', 'b']
for user in new_users:
    if user in current_users:
        print(user + "被使用")
    else:
        print(user + "没有被使用")
