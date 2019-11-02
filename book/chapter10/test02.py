class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_all(self):
        print(self.__name,self.__score)

    def get_name(self):
        return  self.__name

    def get_score(self):
        return  self.__score

    def set_name(self,name):
        self.__name=name

name1=Student('name1',22)
#haha=name1.get_name()
#print(haha)
# name1.set_name('name2')
# new=name1.get_name()
# print(new)
print(name1.get_name())
ss=name1.__name='new name'
print(ss)
print(name1.get_name())