# 1. 문자열 mystring이 주어집니다  x를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return하는 solution함수를 만드시오
def solution(mystring):
    a = list(filter(lambda x:x != "",mystring.split("x")))
    a.sort()

    return a


# 2. 정수배열 arr과 delete_list가 있습니다 arr의 원소중에 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의arr에 있던 순서를 유지한 배열을 return하는 solution1함수를 만드시오
def solution1(arr,delete_list):
   return list(filter(lambda x: x not in delete_list,arr))

# 3. 정수배열 number 가 매개변수로 주어집니다 number의 원소중 두개를 곱해 만들 수 있는 최대값을 return하도록 solution2 함수를 완성하시오
def solution2(number):
    result = 0
    number.sort()
    if number[0]*number[1]>number[-1]*number[-2]:
        return number[0]*number[1]
    else:
        return number[-1]*number[-2]