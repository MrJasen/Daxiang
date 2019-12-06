# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#
#     def power(self):
#         #print(self.x)
#         return self.x * self.x
#
#
# obj = MyObject()
# obj.y=20
# print(obj.y)
# print(hasattr(obj,'power'))
# hasattr()
# setattr()
# getattr()
class Student(object):
    def get_score(self):
        print(self._score)
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("类型不对")
        if value<0 or value>100:
            raise ValueError('范围不对')
        self._score=value

s = Student()
s.set_score(22)
s.get_score()