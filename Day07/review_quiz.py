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


