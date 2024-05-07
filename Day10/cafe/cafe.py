# 카페 기능 사용자가 종료할 수 있는 기능을 포함한다
# while True:
#     x = int(input("숫자를 입력하시오(1. 커피판매 메뉴 2. 커피 메뉴 추가 3. 프로그램 종료):"))
#     if x == 1:
#         print("1.아메리카노 2000원  2.라떼 2500원  3.바닐라라떼 3000원")
#     elif x == 2:
#         int(input("음료를 선택하세요: "))
#         if x == 1:
#             print("아메리카노 2000원 입니다")
#         elif x == 2:
#             print("라떼 2500원 입니다")
#         elif x == 3:
#             print("바닐라라떼 3000원입니다")
#         else:
#             print("메뉴에 있는 숫자를 선택해주세요")
#     elif x == 3:
#         print("프로그램을 종료합니다")
#         break

from coffee import Coffee


#coffeeList = [{'name':'아메리카노','가격':2000},{'name':'라떼','가격':2500},{'name':'바닐라라떼','가격':3000}]
coffeeList = [Coffee("아메리카노",2000),Coffee("라떼",2500),Coffee("바닐라라떼",3000)]
while True:
    x = int(input("(1. 커피판매 2. 커피 메뉴 추가 3. 프로그램 종료):"))
    if x == 1:
        for index, item in enumerate(coffeeList):
            print(f"{index}.{item['name']}:{item['가격']}원")
    elif x == 2:
        newcoffeeName = input("커피 이름: ")
        newcoffeePrice = input("커피 가격: ")
        newcoffeeMenu = {'name':newcoffeeName,'가격':newcoffeePrice}
        coffeeList.append(newcoffeeMenu)
        print(f"{newcoffeeName}이 추가되었습니다")
    elif x == 3:
        print("프로그램을 종료합니다")
        break





