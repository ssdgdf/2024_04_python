# 3. 사용자로부터 정수 n을 입력받아 n의 배수중 짝수만을 출력하는 파이썬 프로그램을 작성해보시오
# num1 = int(input("정수를 입력하시오"))
# for x in range(100):
#     if (num1*x)%2==0 and num1*x<=100:
#         print(num1*x)


# 1.유저에게 다섯개의 정수를 입력받고 리스트화 한 다음 각각 요소를 3배로 만든다음 출력하기
# num1 = int(input("첫번째 정수를 입력하시오"))
# num2 = int(input("두번째 정수를 입력하시오"))
# num3 = int(input("세번째 정수를 입력하시오"))
# num4 = int(input("네번째 정수를 입력하시오"))
# num5 = int(input("다섯번째 정수를 입력하시오"))
# result =[num1*3,num2*3,num3*3,num4*3,num5*3]
# print(result)


# 2. 유저에게 서로다른 다섯개의 정수를 입력받고 리스트화 한다음에 가장큰수를 뽑아내는 프로그램
# numlist = []
# for x in range(5):
#     num = int(input("서로다른 정수를 입력하세요"))
#     numlist.append(num)
#     numlist.sort()
#     numlist.reverse()
# print(f"가장큰수는{numlist[0]}입니다")

# 1. 뉴스기사를 스크랩 해오고 유저가 입력한 단어를 기사에서 그 해당 던어를 모두 대문자화 시켜서 다시 보여주시
# news =("""NEW YORK (AP) — A longtime tabloid publisher was expected Tuesday to tell jurors about his efforts to help Donald Trump stifle unflattering stories
#  during the 2016 campaign as testimony resumes in the historic hush money trial of the former president.""")
# word = input("원하는 단어를 입력하시오")
# Newnews = news.replace(word,word.upper())
# print(Newnews)

# 2. 영어 기사를 스크랩 해오고 단어 사이에🎂넣고 출력하기
news1=("""NEW YORK (AP) — A longtime tabloid publisher was expected Tuesday to tell jurors about his efforts to help Donald Trump stifle unflattering stories
during the 2016 campaign as testimony resumes in the historic hush money trial of the former president.""")
words = news1.split(" ")
news2 = "🎂".join(words)
print(news2)
