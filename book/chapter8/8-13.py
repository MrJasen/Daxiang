def build_profile(first, last, **user_info):
    # 创建一个字典
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# 测试传一个姓，一个名，还有键值对的简介
myname = build_profile('刘', '佳顺', age=16, haha='haha', heihei='heihei')
print(myname)
