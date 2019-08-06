class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def decribe_user(self):
        print("用户的摘要"+self.first_name+self.last_name)

    def greet_user(self,msg):
        self.msg=msg
        print(msg)
    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts+1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)

user1=User('李','呵呵')
user1.decribe_user()
user1.greet_user("真厉害")

user2=User('wang','gat')
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
#重置为0
user2.reset_login_attempts()