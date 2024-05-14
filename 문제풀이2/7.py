# 1.주어진 문자열 word의 각 문자를 정수 n만큼 반복하여 새로운 문자열을 생성하는 프로그램을 작성하시오
# word = input('Enter a word: ')
# count = int(input('Enter a count: '))
#
# newword = ""
# for x in word:
#     newword += x*count
# print(newword)

# 2. 사용자로부터 문자열을 입력받아 그 문자열내의 모든 모음만 대문자로 변환하는 프로그램
# word = input('Enter a word: ')
# new_word = ""
# for x in word:
#     if x in ("a,e,i,o,u") :
#         new_word += x.upper()
#     else:
#         new_word += x
#     print(new_word)

# 3. 입출력의 예 대문자를 소문자로 소문자를 대문자로 변경하는 프로그램
# word = input("Enter a word: ")
# new_word = ""
# for x in word:
#     if x.isupper():
#         new_word += x.lower()
#     else:
#         new_word += x.upper()
# print(new_word)

# 4. 단어를 입력했을때 자음은 대문자화 해서 출력 ex) hello -> HeLLo
word = input("Enter a word: ")
new_word = ""
for x in word:
    if x in "aeiou":     # if x not in "aeiou":
        new_word += x
    else:
        new_word += x.upper()
print(new_word)

# 영어기사 스크랩 해오고 단어 길이가 6글자 이상인 단어들만 출력하기
news = """A wave of pro-Palestinian protests spread and 
intensified on Wednesday as students gathered on campuses around the country, 
in some cases facing off with the police, in a widening showdown over campus speech and the war in Gaza."""
# word = news.split()
# for x in word:
#     if len(x)>=6:
#       print(x)

fruit = ["apple","banana","kiwi","melon","mango","pineapple","strawberry"]
# 문자길이가 5글자 이하이고 알파벳이 a,e가 포함되면 대문자로 그게아니면 그 과일 문자 길이를 출력하는 프로그램
for x in fruit:
    if len(x)<=5 and ("a" in x or "e" in x):
        print(x.upper())

    else:
        print(len(x))