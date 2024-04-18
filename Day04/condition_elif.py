#condition_elif.py
# num = int(input("점수 입력:"))
#
# if num>=90:
#     print("A등급")
# elif num>=80:
#     print("B등급")
# elif num>=70:
#     print("C등급")
# else:
#     print("과락입니다")

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

#nested condtion
# if문의 depth는 2번까지만
score = int(input("Enter your score: "))
if score >= 60:
    if score == 100:
        print("만점입니다")
    else:
        print("합격입니다")
else:
    if score == 0:
        print("이건 좀 ...")
    else:
        print("불합격입니다")