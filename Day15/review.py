# 사용자에게 태어난 년도를 입력받아 그해에 해당하는 띠를 알려주는 기능을 구현하려고 합니다 12간지를 활용하여 태어난 년도를 입력하면 그해의 띠를 반환하는 함수를 작성하시오
def yearTozodiac(year):
    zodiac = {
        0:"원숭이",
        1:"닭",
        2:"개",
        3:"원숭이",
        4:"돼지",
        5:"소",
        6:"쥐",
        7:"호랑이",
        8:"토끼",
        9:"뱀",
        10:"말",
        11:"양",
    }
    return zodiac[year%12]
print(yearTozodiac(2006))


# 자연수 n을 각자리 숫자를 가지는 배열형태 돌려주는 solution함수를 만들어 주세요
def solution(x):
    n = list(str(x))
    n.reverse()
    b = list(map(lambda x:int(x),n))
    return b


def makeReveresedNumber(x):
    return list(map(lambda x: int(x),reversed(list(str(x)))))





# 정수 n을 매개변수로 주어질때 n이하의 홀수가 오름차순으로 담긴 배열을 return 하도록 solution함수를 완성하시오

def solution(num):
     return [x for x in range(num + 1) if x % 2 == 1]

#[x for x in range(10) if x%2==1]


# 랜덤을 사용하여 띠함수 사용하여 100개 띠들이 있는 리스트 만들기
import random

for x in range(101):
 random.randint(1930,2025)

a = [yearTozodiac(random.randint(1930,2025)) for x in range(100)]
print(a)

# random.randit(0,100)
#random.choice(["콜라","사이다","환타","탄산수"])
#random.shuffle(b)
b = ["콜라","사이다","환타","탄산수"]
c = [6,2,1,1]

d = random.choices(b,weights=c,k=10)
print(d)

