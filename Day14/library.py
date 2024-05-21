import math
import random

print(random.randint(0,10000))

# 랜덤으로 여섯개의 숫자를 뽑아주는 프로그램[1~45] 중복x
# lotto = []
# while True:
#     num = random.randint(1,45)
#     if lotto.count(num)==0:
#         lotto.append(num)
#         if len(lotto)==6:
#             break
# lotto.sort()
# print(lotto)

print(random.choice(["사과","배","바나나","집가고싶다"]))

number = int(input("로또 번호 6개를 입력하세요: "))
lotto = []
while True:
    num = random.randint(1,45)
    if lotto.count(num)==0:
        lotto.append(num)
        if len(lotto)==6:
                break
number = [int(input(f"{x}.로또 번호 6개를 입력하세요: ")) for x in range(6)]
rank =6
for x in lotto:
    if number.count(x)>0:
        rank-=1
print(f"로또: {lotto}")
print(f"당신: {number}")
print(f"{rank}등 축하합니다")




