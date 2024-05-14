coffeelist = [{'이름':'아메리카노' , '가격':2500},{'이름':'라떼','가격':3000},{'이름':'핫초코','가격':4000}]
while True:
    x = int(input("(1. 커피판매 2. 커피 메뉴 추가 3. 프로그램 종료):"))
    if x==1:
        for index,item in enumerate(coffeelist):
            print(f"{index}.{item['이름']}:{item['가격']}원")

    if x==2:
        newcoffeename = input("커피이름을 고르시오 ")
        newcoffeeprice = input("커피가격을 고르시오 ")
        newcoffeemenu = [{'이름':newcoffeename},{'가격':newcoffeeprice}]
        coffeelist.append(newcoffeemenu)
        print(f"{newcoffeename}가 추가되었습니다")
    if x==3:
        print("프로그램을 종료합니다")
        break

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
