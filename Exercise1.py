class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        restaurant_name = self.name
        cuisine = self.cuisine_type
        print(f"{restaurant_name} serves best {cuisine} food.")

    def open_restaurant(self):
        msg = self.name
        print(f"{msg} is open.")

restaurant = Restaurant('Taste of Rome', 'Italian')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()