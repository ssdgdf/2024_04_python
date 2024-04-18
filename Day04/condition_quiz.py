# 1.정수를 입력받고
#양의 홀수 , 양의짝수,0,음의홀수,음의짝수
# 판별하는 프로그램
# num = int(input("정수를 입력하시오: "))
# if num>0 and num%2==0:
#     print("양의 짝수입니다")
# elif num>0 and num%2==1:
#     print("양의 홀수입니다")
# elif num<0 and num%2==0:
#     print("음의 짝수입니다")
# elif num<0 and num%2==1:
#     print("음의 홀수입니다")
# elif num==0:
#     print("0입니다")
# else:
#     print("잘못입력하였습니다")
#
#
#
# if num>0:
#     if num%2==1:
#         print("양의 홀수입니다")
#     else:
#         print("양의 짝수입니다")
# elif num==0:
#     print("0입니다")
# else:
#     if num<0:
#         if num%2==1:
#             print("음의 홀수입니다")
#             if num%2==0:
#                 print("음의 짝수입니다")
#
#
#
# num = int(input("정수를 입력하시오"))
# isPositive = num>0
# isNegative = num<0
# isOdd = num%2==1
# isEven = num%2==0
# if isPositive and isOdd:
#     print("양의 홀수입니다")
# elif isPositive and isEven:
#     print("양의 짝수입니다")
# elif isNegative and isOdd:
#     print("음의 홀수입니다")
# elif isNegative and isEven:
#     print("음의 짝수입니다")
# elif:
#     print("0입니다")


# 사용자로 부터 x축과 y축의 좌표값을 x와y를 입력받아 해당 좌표가 좌표평면의 어느 사분면에 위치하는지 판별하는 프로그램
# x = int(input("x축을 입력하시오: "))
# y = int(input("y축을 입력하시오: "))
# if x>0 and y>0:
#     print("입력하신 좌표는 제 1사분면 입니다")
# elif x<0 and y>0:
#     print("입력하신 죄표는 제 2사분면 입니다")
# elif x<0 and y<0:
#     print("입력하신 죄표는 제 3사분면 입니다")
# elif x>0 and y<0:
#     print("입력하신 죄표는 제 4사분면 입니다")
# elif x==0 and y==0:
#     print("입력하신 좌표는 원점 입니다")
# elif x==0:
#     print("y축 위에 존재합니다")
# elif y==0:
#     print("x축 위에 존재합니다")
#

# 사용자로부터 구해한 총 금약을 입력받아 그 금액에 따라 할인율을 적용하는 프로그램
# 5만원 이상이면 5% 10만원이상이면 10% 20만원이상이면 20% 할인적용
price = int(input("구매한 총 금액을 입력하시오"))
sale = price*0.05 # 5만원이상
sale2 = price*0.1 # 10만원 이상
sale3 = price*0.2 # 20만원 이상
if price>=50000 and price<100000:
    print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{sale} 최종금액은{price-sale}입니다")
elif price>=100000 and price<200000:
    print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{sale2} 최종금액은{price-sale2}입니다")
elif price>=200000:
    print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{sale3} 최종금액은{price-sale3}입니다")

# if price>=50000 and price<100000:
#     print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{price*0.05} 최종금액은{price-price*0.05}입니다")
# elif price>=100000 and price<200000:
#     print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{price*0.1} 최종금액은{price-price*0.1}입니다")
# elif price>=200000:
#     print(f"구매금액은 {price} 이고 할인율은{20}% 할인금액은{price*0.2} 최종금액은{price-price*0.2}입니다")
