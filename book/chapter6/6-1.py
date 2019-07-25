# 使用一个字典来存储一个熟人的信息，包括姓、名、年龄、居住城市
# # # 字典包括键first_name、last_name、age和city,并将字典中所有的信息都打印出来
laowang = {
    "first_name": "lao",
    "last_name": "wang",
    "age": "66",
    "city": "beijing",
}
print("老王的姓是: "+laowang["first_name"].title())
print("老王的名是: "+laowang["last_name"].title())
print("老王的年龄是: "+laowang["age"].title())
print("老王的城市是: "+laowang["city"].title())
for key,value in laowang.items():
    print("key: "+key)
    print("value: "+value)

# user = {'username': 'efermi',
#           'first': 'enrico',
#           'last': 'fermi',
#           }
#
# for key, value in user.items():
#     print("\nKey: " + key)
#     print("Value: " + value)