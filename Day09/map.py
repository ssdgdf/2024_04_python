# print,input,sum,len,max,min->기본
# map -> 심화
# map( how, target) : target을 바꿔주기
numlist = [x for x in range(10)]
result = list(map(lambda x: x+100, numlist,)) # [100,101,102,......,200])
print(result)

# filter : targer을 필터링 해줌
result = list(filter(lambda x: x % 2 == 0, numlist))
print(result)

# 글자수 5이상 살리기
fruits = ['apple', 'banana', 'cherry','kiwi']
result = list(filter(lambda x: len(x) >= 5, fruits))
print(result)

# a가 포함된것만 살리기
result = list(filter(lambda x: 'a' in x , fruits))
print(result)

emailLsit = ["abc@naver.com","mega@gmail.com","korea@daum.com"]
# map-> 유저 아이디로 바꾸기
result = list(map(lambda x : x.split("@")[0] , emailLsit))
print(result)
