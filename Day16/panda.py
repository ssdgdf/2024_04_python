import pandas
from faker import Faker
import random

f = Faker('ko_KR')
print(f)







#
# arr = [x for x in range(101)]
# series = pandas.Series(arr)
# #print(series)
#
# data = {
#     'movies':["혹성탈출","범죄도시4","설계자","퓨리오사"],
#     'popcon':["오리지널","어니언","치즈","카라멜"],
#     'beverage':["콜라","제로콜라","사이다","환타"],
# }
#
# df = pandas.DataFrame(data)
# print(df)
#
#
# JS = {
#     'name':["사토루","스쿠나","메구미","유타","하카리","미와","쇼코","게토","토도","토우지"],
#     'age':["24","500","17","19","19","17","24","24","18","31"],
#     'skil':["무량공처","복마어주자","감합암예정","진안상애","좌살박도","신카게류","반전술식","주령조종술","불의유희","천여주박"],
#     'life':["D","L","L","L","L","L","L","D","L","D"]
# }
# a = pandas.DataFrame(JS)
# print(a)
#

majorList = ["국문","일문","영문","중문","노어","철학","문헌정보","경제","경영","통계","사회복지","기계공학","화학공학","전자공학","컴퓨터공학","물리","수학"]


data1 = {
    'name':[f.name() for x in range(1000)],
    'grade':[random.randint(1,5) for x in range(1000)],
    "major":[random.choice(majorList) for x in range(1000)],
    'secore':[round(random.uniform(1,4.5),2) for x in range(1000)]

}
import math
print(round(random.uniform(1,4.5),2))
b = pandas.DataFrame(data1)
b.to_csv('university.csv',index=False, encoding='cp949')
print(b)