# 제어문
# 실행 순서를 조작하는 문법
# 조건문
# if,else,elif

# print("프로그램 시작")
# num = int(input("숫자를 입력 "))
#
# if num>0:
#     print("입력하신 숫자는 양수입니다")
#     print("프로그램 끝")
#
# # 1. 숫자를 입력을 받고 해당 숫자가 100이면 100을 입력 하셨습니다
# print("프로그램 시작")
# num1 = int(input("숫자를 입력"))
# if num1==100:
#     print("100을 입력하셨습니다")
#     print("프로그램 종료")
#
# # 2. 숫자를 입력받고 해당 숫자가 20~30 이면 20에서 30사이에 숫자를 입력하셨습니다
# print("프로그램 시작")
# num2 = int(input("숫자를 입력"))
# if 20<=num2<=30:
#     print("20에서 30사이에 숫자를 입력하셨습니다")
#     print("프로그램 종료")
#
# # 3. 숫자를 입력받고 해당 숫자가 짝수이면 짝수입니다
# print("프로그램 시작")
# num3 = int(input("숫자를 입력"))
# if num3%2==0:
#     print("짝수입니다")
#     print("프로그램 종료")
#
#     # else
#     print("프로그램 시작")
#     num1 = int(input("숫자를 입력"))
#     if num1 >= 0:
#         print("양수입니다")
#     else:
#         print("음수입니다")
#         print("프로그램 종료")


# 비밀번호 입력 프로그램
# ! and IT 가 포함되면 올바르게 비밀번호를 입력하였습니다
# 아니면 올바르게 포함되지 않았습니다
# password = input("비밀번호를 입력:")
# if "!" in password and "IT" in password :
#  print("올바르게 비밀번호를 입력하였습니다")
# else:
#  print("올바르게 포함되지 않았습니다")
#
#
# # 홀수 짝수 반별 프로그램
# num4 = int(input("정수를 입력하시오"))
# if num4%2==0:
#  print("짝수입니다")
# else:
#  print("홀수입니다")

    # 비밀번호 설정
    # ! 포함되지 않고 첫번쨰 글자가 a or A이여야 올바른 비밀번호이다
password = input("비밀번호를 입력 : ")
if not ('!' in password) and (password[0]=='a'or'A'):
    print("비밀번호를 올바르게 설정했습니다")
else:
    print("비밀번호를 올바르지 못하게 설정했습니다")
