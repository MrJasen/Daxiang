#coding=utf-8
import  json

class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    #写一个转换函数，把对象转为dict
    def student2dict(std):
        return {
            'name':std.name,
            'age':std.age,
            'score':std.score
        }
s=Student('jason',20,30)
print(json.dumps(s,default=student2dict))