# control statement
# condition statement[조건문]
# if 조건
#[들여쓰기] 코드
# elif 조건:
# else:
# pass 는 코드를 넘겨주는 역활

# loop statment[반복문]
# for문 :  개발자가 끝이 언제인지 알 떄
# for x in range(n)->0~n-1
# for x in "hello" -> h,e,l,l,o
# for x in [1,2,3,4,5]->1,2,3,4,5
# for x,y in dict.item() -> k,v/k,v/k,v
# for x in set -> a,b,c,d (순서 보장 안됨)
coffee = {"name":"아메리카노","price":3000}
for x,y in coffee.items():
    print(f"{x},{y}")

# while 문 : 개발자가 끝이 언제일지 모를 때
# while문 조건:
#       로직
#       무한 루프 막는 방법:  break or 조건 구하기
#
#
#

