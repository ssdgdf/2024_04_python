# comprehension
#[0~100]리스트 출력
numlsit = []
for x in range(101):
    numlsit.append(x)
print(numlsit)


a = [x for x in range(101)]
print(a)


# "apple" => [a,p,p,l,e]
b = [x for x in "apple"]

# [0~10]
c = [x for x in range(11) if x % 2 == 0]

# 0~100 까지 홀수만
d = [x for x in range(101) if x%2==1]

# 0~100 짝수를 제곱인 상태로 리스트
e = [x**2 for x in range(101) if x%2==0]

# 0~10 홀수에서 10을 더한 리스트
f = [x+10 for x in range(10) if x%2==1]
print(f)


fruits = ["apple", "orange", "pear","kiwi","banana"]
g = [len(x) for x in fruits]
print(g)

h = [len(x) for x in fruits if 'i' in x]
print(h)

# 메핑 컴프리헨션
# 홀수는 10 짝수는 20
i = [x+10 if x%2==1 else x+20 for x in range(101)]
print(i)

# 5글자 이하이면 글자의 길이를 아니면 대문자화 하기
fruits = ["apple", "orange", "pear","kiwi","banana"]
j = [len(x) if len(x)<=5 else x.upper() for x in fruits]
print(j)