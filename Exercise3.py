class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        restaurant_name = self.name
        cuisine = self.cuisine_type
        print(f"{restaurant_name} serves best {cuisine}.")

    def open_restaurant(self):
        msg = self.name
        print(f"{msg} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("Flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


frozen_bottle = IceCreamStand('Frozen Bottle')
frozen_bottle.flavors = ['strawberry','vanilla', 'fig & honey']

frozen_bottle.describe_restaurant()
frozen_bottle.show_flavors()