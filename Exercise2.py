class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        restaurant_name = self.name
        cuisine = self.cuisine_type
        print(f"{restaurant_name} serves best {cuisine} food.")

    def open_restaurant(self):
        msg = self.name
        print(f"{msg} is open.")

    def set_number_served(self, number_served):
        if type(number_served) not in [int]:
            raise TypeError("The value sholud be a non negative real number.")
        if number_served < 0:
            raise ValueError("number_served cannot be negative.")
        else:
            self.number_served = number_served

    def increment_number_served(self, additional_served):
        if type(additional_served) not in [int]:
            raise TypeError("The value sholud be a non negative real number.")
        if additional_served < 0:
            raise ValueError("additional_served cannot be negative.")
        else:
            self.number_served += additional_served


restaurant = Restaurant('Taste of Rome', 'Italian')
restaurant.describe_restaurant()

print(f"Number served: {str(restaurant.number_served)}")
restaurant.number_served = 100
print(f"Number served: {str(restaurant.number_served)}")

restaurant.set_number_served(200)
print(f"Number served: {str(restaurant.number_served)}")

restaurant.increment_number_served(300)
print(f"Number served: {str(restaurant.number_served)}")