class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("restaurant name :" + self.restaurant_name)
        print("restaurant cuisine type: " + self.cuisine_type)
        pass
    def is_open(self):
        print(self.restaurant_name + " is open")
        pass
my_restaurant = Restaurant('chinese','kongpaochinken')
my_restaurant.describe_restaurant()
my_restaurant.is_open()

