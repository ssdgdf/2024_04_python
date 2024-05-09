# x: 1, "abc@naver.com",[],{},......
# x: 함수도 들어갈 수 있습니다
# f(x)
import monster


def a(x):
    print("a함수 실행")
    x()

def b():
    print("b함수 실행")
a(b)

# 게임 몬스터 프로그램
# f(g(x))
def killing_monster(monster,event):
    print(f"{monster}를 처치 하였습니다")
    event()
    #골드 or 음식 or 경험치
def getGold():
    print("골드 획득")

def getFood():
    print("식량 획득")

killing_monster( "슬라임" , getGold)
killing_monster( "늑대" , getFood)
