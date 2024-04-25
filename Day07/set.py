# set(집합)
# 중복 허용 안되는 타입
a = {1,2,3,4,5,6,7,8}
burgerkong = {"와퍼","새우 와퍼","치즈와퍼","스테이크 와퍼"}
momstouch = {"와퍼","새우 와퍼","싸이버거","불고기 와퍼"}
x = burgerkong.intersection(momstouch)
print(x)

# 합집합(|)
union = burgerkong | momstouch

# 교집합(&)
intersection = burgerkong & momstouch

# 차집합(-)
difference = burgerkong - momstouch

print(union)
print(intersection)
print(difference)

# 추가
burgerkong.add("모짜렐라 와퍼")

# 전체삭제
burgerkong.clear()

# 삭제
#burgerkong.remove("새우 와퍼")# 구문법 없는 요소 빼면 에러
#burgerkong.discard("새우 와퍼")# 신문법 없는 요소 빼면 에러 발생 안함

# set()
result = set([1,2,3,1,2,3])
print(list(result))

news = """A wave of pro-Palestinian protests spread and intensified on Wednesday
 as students gathered on campuses around the country, in some cases facing off with the police, 
 in a widening showdown over campus speech and the war in Gaza."""
wordlist = news.split()
noDuplicationWords = list(set(wordlist))
noDuplicationWords.sort()
print(noDuplicationWords)
