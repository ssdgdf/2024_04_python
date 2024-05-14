# 1. 사용자로부터 전체 이메일주소를 입력받습니다  프로그램은 입력받은 이메일 주소에서 사용자 이름 부분과 도메인 부분을 분리하여 출력합니다
def email(x):
    arr = x.split('@')
    return {"user":arr[0] , "email adress":arr[1]}
print(email("rhwndud777@naver.com"))

# 2. 사용자로부터 문자열을 입력받습니다 입력된 문자열은 두가지 마법적 변환을 거치게 됩니다 하나는 문자열을  뒤집어 순서를 바꾸고
# 다른 하나는 문자열의 알파벳 순서로 정렬합니다
def word(x):
    newword = list(x)
    newword.sort()
    result = "".join(newword)

    newword2 = list(x)
    newword2.reverse()
    result2 = "".join(newword2)
    return {"sorted":newword , "reverse" : newword2}
print(word("newwebtoon"))


# 3. 정수 n이 주어졌을때 홀수면 "odd" 짝수면 "even"을 돌려주는 함수 만들기
def num(x):
    if num%2==0:
        return "even"
    else:
        return "odd"

# 함수를 간략화 해주는게 lambda
def add(x, y):
    return x + y
lambda x,y:x+y
# x,y 빼는거 lambda x,y:x-y
# x의 제곱   lambda x:x**2
# 문자열의 길이의 제곱  lambda x:len(x)**2

numlist = [x for x in range(10)]
result = list(map(lambda x: x+100, numlist,)) # [100,101,102,......,200])
print(result)

# filter : targer을 필터링 해줌
result = list(filter(lambda x: x % 2 == 0, numlist))
print(result)