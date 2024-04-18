# 반복문(loop)
# for 반복문
# for 미지수 in range(n번):
# print,input,str,int,float,bool,type
#range(n): 0~n-1까지 순회해줘

# for x in range(10):
#     print(f"{x}. hello")
#
# num = int(input("몇번 실행 할까요: "))
# for x in range(num):
#     print(f"{x}. hello world")


# 0~200까지 찍히는 프로그램을 만드세요
for x in range(201):
    print(x)

# 0~200까지 짝수만 찍히는 프로그램을 만드세요
for x in range(201):
    if x % 2 == 0:
     print(x)

# 0~1000 까지 3의배수만 찍히도록 만드시오
for x in range(1001):
    if x %3==0:
     print(x)

# 구구단
# 유저에게 몇단을 입력하면 해당 단을 모두 보여주는 프로그램
num = int(input("단을 입력하시오 : "))
for x in range(10):
    print(f"{num*x}")