# from Coffee.coffee import Coffee
# from Inventory.inventory import Inventory
#
# itkoreaInventory = Inventory()
# itkoreaInventory.add_coffee(Coffee("아메리카노",2500))
# itkoreaInventory.add_coffee(Coffee("민초프라프치노",4500))
# itkoreaInventory.add_coffee(Coffee("흑임자라떼",3500))
#
# a = itkoreaInventory.get_inventory()
# print(a)
# print(a['흑임자라떼'])
# print(a['흑임자라떼'].get_name())
# print(a['흑임자라떼'].get_price())


from App.app import Application

program = Application()
program.run()
