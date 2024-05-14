class Inventory:
    def __init__(self):
        self.item = {}

    def add_coffee(self,coffee):
        self.item[coffee.get_name()] = coffee

    def get_inventory(self):
        return self.item