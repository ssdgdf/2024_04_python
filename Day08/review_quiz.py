# 1.양의정수 n을 매개변수로 받아들여 n의 홀짝성에 따라 다른 계산을 수행하는 프로그램을 작성하시오
# num = int(input("정수를 입력하세요 : "))
# result = 0
# if num%2 == 1:
#     for x in range(num+1):
#         if x%2 == 1:
#             result += x
# else:
#     for x in range(num+1):
#         if x%2 == 0:
#             result += x**2
# print(result)

# 2. 정수배열 arr와 자연수k가 주어집니다 이때 k의 홀짝성에 따라 배열에 다른 연산이 적용됩니다 만약k가 홀수라면 배열arr의 모든 원소에 k를 곱하고
# k가 짝수이면 모든 원소에 k를 더합니다
k = int(input("정수를 입력하시오 : "))
arr = [1,2,3]
result = []
if k%2 == 1:
    for i in arr:
        result.append(i*k)
else:
    for i in arr:
        result.append(i+k)
print(result)

