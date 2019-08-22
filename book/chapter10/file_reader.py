# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#     #file_object.close()

# file_path=r'D:\大象学院\book\chapter10\file_1\file_2\text.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#     #file_object.close()

# with open('pi_digits.txt') as file_object:
#     lines =file_object.readlines()
# pi_string=''
# for line in lines:
#     pi_string=pi_string+line.strip()
# print(pi_string[:7])
# print(len(pi_string))

# with open('pi_digits.txt') as file_object:
#     lines=file_object.readlines()
# pi_str=''
# for line in lines:
#     pi_str=pi_str+line.rstrip()
# print(pi_str)
filename= 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string=''
for line in lines:
    pi_string=pi_string+line.strip()
birthday=input("请输入生日")
if birthday in pi_string:
    print('in')
else:
    print("not in")