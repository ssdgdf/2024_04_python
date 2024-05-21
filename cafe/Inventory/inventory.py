class Inventory:
    def __init__(self):
        self.item = {}

    def add_product(self,product):
        self.item[product.get_name()] = product

    def get_inventory(self):
        return self.item