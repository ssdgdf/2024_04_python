#loop_while.py

# x = 10
# while x >0:
#     print("불금인데 학원온거 ㅇㅈ?")
#     x -=1 # x=x-1
#
# x=-1
# while True:
#     x= int(input("숫자를 입력하시오( 단0 을넣어으면  멈춤) :"))
#     if x==0:
#         break

# 1=아이스 아메리카노 2=아이스라떼 0=멈춤
# while True:
#     x= int(input("숫자를 입력하시오( 단0 을넣어으면  멈춤) :"))
#     if x==1:
#         print("아메리카노")
#     elif x==2:
#         print("아이스 라떼")
#     elif x==0:
#         break

# 유저에게 언어를 고르시오
# 1.파이썬 2.자바 3.c언어 4.프로그램 종료
# while True:
#     x= int(input("원하는 언어 숫자를 입력하시오(1.파이썬 2.자바 3.c언어 4.프로그램 종료) :"))
#     if x==1:
#         print("파이썬")
#     elif x==2:
#         print("자바")
#     elif x==3:
#         print("c언어")
#     elif x==4:
#         print("프로그램 종료")
#         break
#     else:
#         print("숫자를 잘못 입력하였습니다")

# 계산기 프로그램
# 유저에게 1.더하기 2.빼기 3.곱하기 4,제곱 5.나누기
#1-> 두정수를 입력하고 더할 결과값나옴
while True:
    x = int(input("원하는 언어 숫자를 입력 하시오(0.종료 1.더하기 2.빼기 3.곱하기 4,제곱 5.나누기) :"))
    if x==1:
        num1 = int(input("첫번째 정수를 입력하시오"))
        num2 = int(input("두번째 정수를 입력하시오"))
        print(f"두 정수의 합은{num1+num2}입니다")
    elif x==2:
        num1 = int(input("첫번째 정수를 입력하시오"))
        num2 = int(input("두번째 정수를 입력하시오"))
        print(f"두 정수의 차는{num1-num2}입니다")
    elif x==3:
        num1 = int(input("첫번째 정수를 입력하시오"))
        num2 = int(input("두번째 정수를 입력하시오"))
        print(f"두 정수의 곱은{num1*num2}입니다")
    elif x==4:
        num1 = int(input("첫번째 정수를 입력하시오"))
        num2 = int(input("두번째 정수를 입력하시오"))
        print(f"두 정수의 제곱은{num1**num2}입니다")
    elif x==5:
        num1 = int(input("첫번째 정수를 입력하시오"))
        num2 = int(input("두번째 정수를 입력하시오"))
        print(f"두 정수의 나누기 는 {num1/num2}입니다")
    elif x==0:
        print("프로그램이 종료 됩니다")
        break


