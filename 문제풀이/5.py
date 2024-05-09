# 유저에게 과일을 영어로 3개 입력받고
# 과일 리스트를 만들고 오름차순으로 보여주기
# f1 = input("첫번째 과일을 입력하시오")
# f1.upper()
# f2 = input("두번째 과일을 입력하시오")
# f2.upper()
# f3 = input("세번째 과일을 입력하시오")
# f3.upper()
#
# fruit = []
# fruit.append(f1)
# fruit.append(f2)
# fruit.append(f3)
# print(fruit)

# 4.사용자로부터 정수를 입력받아 해당정수의 배수를 100까지 출력하시오
# num1 = int(input("정수를 입력하세요"))
# for x in range(101):
#     if num1*x<101:
#      print(f"{num1*x}")


#유저에게 과일을 입력받고
#모음을 제거한 단어로 나타내기 apple -> ppl  ,  banana->bnn ,
# fruit = input("과일을 입력하시오")
# word=""
# for x in fruit:
#     if not x in 'aeiou':
#         word += x
# print(word)


# 1.1~100까지 총합을 나타내는 프로그램
total = 0
for x in range(101):
    total = x+total
print(total)


