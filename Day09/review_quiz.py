# 1. 사용자로부터 전체 이메일주소를 입력받습니다  프로그램은 입력받은 이메일 주소에서 사용자 이름 부분과 도메인 부분을 분리하여 출력합니다
def email(x):
    arr = x.split("@")
    return {"user": arr[0], "domain": arr[1]}
print(email("rhwndud777@naver.com"))

# 2. 사용자로부터 문자열을 입력받습니다 입력된 문자열은 두가지 마법적 변환을 거치게 됩니다 하나는 문자열을  뒤집어 순서를 바꾸고
# 다른 하나는 문자열의 알파벳 순서로 정렬합니다
"mega"
def magic(word):
    newlist = list(word) #[m,e,g,a]
    newlist.sort() #[a,e,g,m]
    result = "".join(newlist) # list->str

    newlist1 = list(word)
    newlist1.reverse()
    result1 = "".join(newlist1)
    return {"sorted": result, "reversed": result1}

print(magic("newwebtoon"))

# 3. 정수 n이 주어졌을때 홀수면 "odd" 짝수면 "even"을 돌려주는 함수 만들기
def number(n):
    if n%2 == 0:
        return "odd"
    else:
        return "even"



