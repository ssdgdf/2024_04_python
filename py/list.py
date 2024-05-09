# 유저에게 과일을 영어로 3개 입력받고
# 과일 리스트를 만들고 오름차순으로 보여주기
fruit1=input("과일을 입력하시오 : ")
a=fruit1.upper()
fruit2=input("과일을 입력하시오 : ")
b=fruit2.upper()
fruit3=input("과일을 입력하시오 : ")
c=fruit3.upper()

fruit = []
fruit.append(a)
fruit.append(b)
fruit.append(c)
fruit.sort()
print(fruit)





fruits = ["apple", "banana", "kiwi", "mango"]
numbers = [1, 2, 3, 4, 5]
mix = ["안녕",1,"집에 갈레",2,True,[]]
cafe = [["아메리카노","라떼"],["쥬스","에이드"],["빵","케이크"]]
print(cafe[0][1]) # 라떼
print(cafe[2][0]) # 빵

#kiwi == fruits[2]
print(fruits[1].upper())


# append[추가하기]
fruits.append("orange")
print(fruits)

#extend[확장하다]
fruits.extend(["strawberry", "pear"])
print(fruits)

# sort[정렬하다]
fruits.sort()
print(fruits)

#reverse[반대로 하다]
fruits.reverse()
print(fruits)

# pop[튀다]
fruits.pop()
print(fruits)

# remove[제거하다]
fruits.remove("pear")
print(fruits)

#count
fruits.append("banana")
x=fruits.count("banana")
print(x)

# for 리스트는 요소를 하나씩 빼준다
for x in fruits:
    print(x)