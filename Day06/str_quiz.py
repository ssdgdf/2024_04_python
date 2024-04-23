# 1. 뉴스기사를 스크랩 해오고 유저가 입력한 단어를 기사에서 그 해당 던어를 모두 대문자화 시켜서 다시 보여주시
# news =("""NEW YORK (AP) — A longtime tabloid publisher was expected Tuesday to tell jurors about his efforts to help Donald Trump stifle unflattering stories
# during the 2016 campaign as testimony resumes in the historic hush money trial of the former president.""")
# word = input("원하는 단어를 입력하시오 : ")
# newnews = news.replace(word,word.upper())
# print(newnews)


# 2. 영어 기사를 스크랩 해오고 단어 사이에🎂넣고 출력하기
news=("""NEW YORK (AP) — A longtime tabloid publisher was expected Tuesday to tell jurors about his efforts to help Donald Trump stifle unflattering stories
during the 2016 campaign as testimony resumes in the historic hush money trial of the former president.""")
words = news.split(" ")
news1 = "🎂".join(words)
print(news1)