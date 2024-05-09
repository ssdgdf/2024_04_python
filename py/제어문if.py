# 제어문 if 문
 # 2. 숫자를 입력받고 해당 숫자가 20~30 이면 20에서 30사이에 숫자를 입력하셨습니다
print("프로그램 시작")
num2 = int(input("숫자를 입력"))
if 20<=num2<=30:
     print("20에서 30사이에 숫자를 입력하셨습니다")
     print("프로그램 종료")

# 비밀번호 입력 프로그램
# ! and IT 가 포함되면 올바르게 비밀번호를 입력하였습니다
# 아니면 올바르게 포함되지 않았습니다
password = input("비밀번호를 입력:")
if "!" in password and "IT" in password :
 print("올바르게 비밀번호를 입력하였습니다")
else:
 print("올바르게 포함되지 않았습니다")


# 홀수 짝수 반별 프로그램
num4 = int(input("정수를 입력하시오"))
if num4%2==0:
 print("짝수입니다")
else:
 print("홀수입니다")

    # 비밀번호 설정
    # ! 포함되지 않고 첫번쨰 글자가 a or A이여야 올바른 비밀번호이다
password = input("비밀번호를 입력 : ")
if not ('!' in password) and (password[0]=='a'or'A'):
    print("비밀번호를 올바르게 설정했습니다")
else:
    print("비밀번호를 올바르지 못하게 설정했습니다")

# elif
# 국영수 점수를 3가지 입력받고
# 평균이 90이상a 80이상B~60이상D
#나머자 F로 보내기
# kor = input("국어점수 입력하기")
# en = input("영어점수 입력하기")
# math = input("수학점수 입력하기")
# over = (int(kor) + int(en) + int(math))/3
# if over>=90:
#     print("A등급입니다")
# elif over>=80:
#     print("B등급입니다")
# elif over>=70:
#     print("B등급입니다")
# elif over>=60:
#     print("B등급입니다")
# else:
#     print("F입니다")