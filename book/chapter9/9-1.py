class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("餐厅名字是"+self.restaurant_name)
        print("餐厅类型是"+self.cuisine_type)

    def open_restaurant(self):
        print("正在营业")

restaurant=Restaurant('old school','og')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2=Restaurant('hiphop','hotdog')
restaurant2.describe_restaurant()