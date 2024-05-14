# 1.양의정수 n을 매개변수로 받아들여 n의 홀짝성에 따라 다른 계산을 수행하는 프로그램을 작성하시오
# num = int(input("정수를 입력하세요"))
# result =0
# if num%2==0:
#     for x in range(num+1):
#         if x%2==0:
#             result += x
# else:
#     for x in range(num+1):
#         if x%2==1:
#             result +=x**2
# print(result)

# 2. 정수배열 arr와 자연수k가 주어집니다 이때 k의 홀짝성에 따라 배열에 다른 연산이 적용됩니다 만약k가 홀수라면 배열arr의 모든 원소에 k를 곱하고
# k가 짝수이면 모든 원소에 k를 더합니다
# arr = [1,2,3,4,5]
# num = int(input("정수를 입력하세요"))
# result = []
# if num%2==0:
#     for x in arr:
#         result.append(x+num)
# else:
#     for x in arr:
#         result.append(x*num)
# print(result)


# comprehension
#[0~100]리스트 출력
numlsit = []
for x in range(101):
    numlsit.append(x)
print(numlsit)


a = [x for x in range(101)]
print(a)

c = [x for x in range(11) if x%2==0]
print(c)

# 5글자 이하이면 글자의 길이를 아니면 대문자화 하기
fruits = ["apple", "orange", "pear","kiwi","banana"]
h = [len(x) for x in fruits if 'i' in x]
print(h)

b = [len(x) if len(x)<=5 else x.upper() for x in fruits  ]
print(b)

# 메핑 컴프리헨션
# 홀수는 10 짝수는 20
i = [x+10 if x%2==1 else x+20 for x in range(101)]
print(i)


# 어떠한 단어를 넣었을 때 그 단어가 6글자 이상이면 글자가 길어요 아니면 글자가 짧아요
def word(x):
     if len(x)>=6:
         return "글자가 길어요"
     else:
         return "글자가 짧아요"
