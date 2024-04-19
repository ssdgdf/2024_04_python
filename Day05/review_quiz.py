# # 1.사용자로 부터 3개의 정수를 입력받아 평균을 계산하시오
# num1 = int(input("첫번째 정수를 입력하시오 : "))
# num2 = int(input("두번째 정수를 입력하시오 : "))
# num3 = int(input("세번째 정수를 입력하시오 : "))
# avg = (num1 + num2 + num3) / 3
# print(f"평균은{avg}입니다")
#
# # 2. 사용자로부터 3개의 정수를 입력받아 가장큰 정수를 찾아 출력하시오
# num1 = int(input("첫번째 정수를 입력하시오 : "))
# num2 = int(input("두번째 정수를 입력하시오 : "))
# num3 = int(input("세번째 정수를 입력하시오 : "))
# if num1 > num2 and num1 > num3:
#     print(f"가장큰 수는 {num1}입니다")
# elif num2 > num1 and num2 > num3:
#     print(f"가장큰 수는 {num2}입니다")
# elif num3 > num1 and num3 > num2:
#     print(f"가장큰 수는 {num3}입니다")
#
# # 3. 비밀번호를 입력받아 특정 조건을 만족하는지 검사하는 프로그램
# password = input("비밀번호를 입력하시오 :")
# check = '!' in password and 'IT' in password
# print(check)


# 4.사용자로부터 정수를 입력받아 해당정수의 배수를 100까지 출력하시오
num = int(input(" 정수를 입력하시오 : "))
for i in range(101):
    if num*i<=100:
     print(num*i)

num = int(input(" 정수를 입력하시오 : "))
for i in range(101):
    if i%num==0:
     print(i)