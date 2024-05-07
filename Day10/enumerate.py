# enumerate
# fruits = ['apple', 'orange', 'mango']
# for x in fruits:
#     print(x)
#
# number = 0
# for x in fruits:
#     print(f"{number}.{x}")
#     number += 1
#
# for index ,item in enumerate(fruits):
#     print(f"{index}.{item}")

coffeeList = [{'name':'아메리카노','가격':2000},{'name':'라떼','가격':2500},{'name':'바닐라라떼','가격':3000}]
for index,item in enumerate(coffeeList):
    print(f"{index}.{item['name']}.{item['가격']}원")