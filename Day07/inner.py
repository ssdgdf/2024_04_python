# "hello".upper() => Hello
# [].append("사과") => ["사과"]

# print,input,str,lsit,int,float,bool,range,type

#length
# len : 문자열 또는 리스트의 길이를 알려주는 기능
# print(len("hello"))
# print(len("python"))
# print(len([1,2,3,4,5]))
#
# # max,min
# print(max([1,5,14,24,75]))
# print(min([1,5,14,24,75]))
#
# # sum
# print(sum([1,2,3,4,5]))

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