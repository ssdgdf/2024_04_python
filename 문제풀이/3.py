# 비밀번호 입력 프로그램
# ! and IT 가 포함되면 올바르게 비밀번호를 입력하였습니다
# 아니면 올바르게 포함되지 않았습니다
# password = input("비밀번호를 입력하세요")
# if '!' and 'IT' in password:
#     print("올바르게 입력하였습니다")
# else:
#  print("비밀번호를 다시 입력하세요")


# 비밀번호 설정
# ! 포함되지 않고 첫번쨰 글자가 a or A이여야 올바른 비밀번호이다
# password = input("비밀번호를 입력하세요")
# if  not ('!' in password) and (password[0]=='a'or'A'):
#     print("올바른 비밀번호 입니다")
# else:
#     print("올바르지 않은 비밀번호 입니다")


# 3.사용자로 부터 원의 반지름을 입력 받아 그원의 둘레와 넓이를 계산 하는 프로그램을 만들어 보시오
ri = int(input("원의 반지름을 입력하시오"))
s1 = ri*ri*3.14
s2 = 2*ri*3.14
print(f"원의 넓이는{s1}이고 둘레는{s2}이다")