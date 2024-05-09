# 기본 자료 구조 : 데이터를 어떻게 보관하는지 다루는지에 대한 방법들
# list, set, dict
# list : 순서 있고 , 중복 가능
# set : 순서 없고 중복 불가능
# dict : k[중복 안됨]-v[중복 가능] 형태로 저장
# tuple : (사과,바나나,키위) 수정 불가능
names = ['아메리카노','라떼','바닐라']
prices = [2000,3000,4000]
menu = []
for index,item in enumerate(names):
    menu.append({'name':item,'price':prices[index]})
    print(menu[index])

x = dict(zip(names,prices))
print(x)


# 과일 이름 리스트[3]
# 과일 가격 리스트[3]
name = ['apple','banana','pear']
price = [2000,3000,4000]

for (x,y) in zip(name,price):
    print(f"{x},{y}")

for index,(x,y) in enumerate(zip(name,price)):
    print(f"{index},{x},{y}")

menu = [{'name':x,'price':y} for (x,y) in zip(name,price)]
print(menu)

# menu= [{'name':'아메리카노','price':2000},{'name':'라떼','price':3000}


names =['아메리카노','라떼','바닐라']
prices = [2000,3000,4000]
for index,item in enumerate(names):
    print(f"{index}.{item}:{prices[index]}")

menu = [{'name':x,'price':y} for(x,y) in zip(names,prices)]
print(menu)


text = "apple banana apple strawberry banana"
a = [{"단어":x,"글자수":len(x)} for x in text.split(" ")]
print(a)

# 심화 자료 구조:
# graph : 그래프 자료구조[지도,미니맵,경로 최적화]
# tree : 트리 자료구조[단어 검색]
# stack : 
#
#



