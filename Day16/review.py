# 1. 정수배열 arr과 자연수 k 가 주어집니다 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고 짝수면 k를 더합니다 이후에는 리턴하는 함수를 만드시오
def solution(arr,k):

#     self.arr = arr
#     self.k = k
#     arr = [1,2,3,4,5]
#     result = []
#     if k%2==0:
#         arr = [1+k,2+k,3+k,4+k,5+k]
#         return arr
#     else:
#         arr = [1*k,2*k,3*k,4*k,5*k]
#         return arr

    return [x*k if k%2==1 else x+k for x in arr ]
arr1 = [21,2,3,100,99,98]
print(solution(arr1,k=2))

# 2. 문자열 mystring이 주어집니다 알파벳'a'가 등장하면 전부'A'로 변환하고 'A'가 아닌 대문자는 소문자로 변환하여 반환하는 함수
def solytion1(mystring):
    # self.mystring = mystring
    # result = ""
    # for x in range():
    #     if mystring in 'a':
    #         result +="A"
    #         return mystring
    #     else:
    #         if mystring not in 'A':
    #             result.lower()
    #             return mystring
    return "".join(['A' if x=='a' else x.lower() for x in "abstracrt algerra"])

# 오늘 낳짜 [05-24,05 25,----ㅡ6-24]
import datetime
def solution2():
    today = datetime.date.today()
    future_time = today+datetime.timedelta(days = 1)
    return future_time.strftime("%m-%d")

a = [solution2(x) for x in range(31)]
print(a)