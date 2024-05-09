# 1.사용자로부터 정삼각형의 밑변과 높이를 입력받아 그 정삼각형의 넓이를 계산하는 프로그램
# num1 = int(input("삼각형의 밑변을 입력하세요"))
# num2 = int(input("삼각형의 높이를 입력하세요"))
# result = (num1*num2)*0.5
# print(f"삼각형의 넓이는{result}이다")

# 2.사용자로부터 하나의 정수를 입력받아 해당 숫자가 양수이면서 동시에 홀수인지를 판별하는 프로그램
# num1 = int(input("정수하나를 입력하세요"))
# if num1>0 and num1%2==1:
#     print("양수이면서 홀수입니다")
# else:
#     print("양수,홀수가 아닙니다")

# 3.사용자로부터 과일의 이름을 입력받아 해당 과일에 알파벳'a'가 포함되는지 검사하는 프로그램
# fruit = input("과일이름을 영어로 입력하세요")
# if 'a' in fruit:
#     print("a가 포합되었습니다")
# else:
#     print("a가 포함되지 않았습니다")

# 국영수 점수를 3가지 입력받고
# 평균이 90이상a 80이상B~60이상D
#나머자 F로 보내기
# kor = int(input("국어점수 입력하기"))
# en = int(input("영어점수 입력하기"))
# ma = int(input("수학점수 입력하기"))
# total = (kor+en+ma)/3
# if total>=90:
#     print("A")
# elif 90>total>=80:
#     print("B")
# elif 80>total>=70:
#     print("C")
# elif 70>total>=60:
#     print("D")
# elif 60>total>=50:
#     print("E")
# else:
#     print("F")


# 사용자로부터 구매한 총 금약을 입력받아 그 금액에 따라 할인율을 적용하는 프로그램
# 5만원 이상이면 5% 10만원이상이면 10% 20만원이상이면 20% 할인적용
buy = int(input("구매한 총 금액을 입력하시오"))
if 100000>buy>=50000:
    print(f"구매금액은{buy}이고 할인율은{(buy*0.05)}이고 총금액은{buy-(buy*0.05)}입니다")
elif 100000<=buy<200000:
    print(f"구매금액은{buy}이고 할인율은{(buy * 0.1)}이고 총금액은{buy - (buy * 0.1)}입니다")
elif 200000<=buy:
    print(f"구매금액은{buy}이고 할인율은{(buy * 0.2)}이고 총금액은{buy - (buy * 0.2)}입니다")

# 구구단
# 유저에게 몇단을 입력하면 해당 단을 모두 보여주는 프로그램
num1 = int(input("몇단을 고르시오"))
for x in range(10):
    print(f"{num1*x}")
