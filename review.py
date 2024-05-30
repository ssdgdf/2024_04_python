# 1. 문자열 my_str과  n이 매개변수로 주어질때 my_str을 길이 n씩 잘라서 저장한 배열을 return하는 함수를 만드시오
def solution(my_str,n):
    arr = []
    word = ""
    for index, item in enumerate(my_str,1):
        word+=item
        if index%n==0:
            arr.append(word)
            word=""
    arr.append(word)
    print(arr)
    return arr



# 2. Jaden Case란 모든 단어의 첫 문자가 대문자이고 그 외의 알파벳은 소문자인 문자열입니다 단 첫문자가 알파벳이 아닐때에는 이어지는 알파벳은 소문자로 쓰면 됩니다
# 문자열 s가 주어졌을때 s를 Jaden Case로 바꾼 문자열을 리턴하는 함수를 작성하시오
def solution1(s):
    return "".join([x.capitalize() for x in s.split(" ")])

print(solution1("for the last week"))

