class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("餐厅名字是"+self.restaurant_name)
        print("餐厅类型是"+self.cuisine_type)
        print("餐厅一共有"+str(self.number_served)+"人就餐过")

    def open_restaurant(self):
        print("正在营业")

    def update_people(self,number):
        self.number_served=number

    def increment_number_served(self,newnumber):
        self.number_served=self.number_served+newnumber

restaurant=Restaurant('old school','og')
restaurant.number_served=11 #直接修改属性
#restaurant.update_people(20) #通过方法来修改
restaurant.increment_number_served(5)
restaurant.describe_restaurant()