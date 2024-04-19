# 어떠한 타입. 그 관련된 기능
#list_type
food = ["돈까스","치킨","타르트","케이크"]
print(food[1]) #치킨
food.append("라멘")
print(food)
food.sort()
print(food)


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
