#메가커피/당일매출 기록표  이름,메뉴,몇시,결제수단,포장여부
import datetime

import pandas
from faker import Faker
import random
f = Faker('ko_KR')


menuList = ["아메리카노","라떼","아이스티","콜드부르","아인슈페너","미숫가루","오레오쉐이크","딸기스무디","망고스무디","옛날커피","모히또에이드","핫초코","뱅쇼","녹차쉐이크","밀크쉐이크"]
buyList = ["현금","카드","삼성페이","애플페이","카카오페이","계좌이체"]
takeoutList = ["테이크아웃","매장식사"]

# def get_time():
#     s = datetime.datetime.strftime("07:00","%H:%M")
#     e = datetime.datetime.strftime("22:00","%H:%M")
#     total = int((e-s).total_secound()/60) # 전체 몇분
#     random_minutes = random.randint(0,total)
#     return s+datetime.timedelta(minutes=random_minutes)

cus = {
    'name':[f.name()  for x in range(1000)],
    'menu':[random.choice(menuList) for x in range(1000)],
   # 'time':[random.randint(0,24) for x in range(1000)],
    'buy':[random.choice(buyList) for x in range(1000)],
    'takeout':[random.choice(takeoutList) for x in range(1000)]
}

df = pandas.DataFrame(cus)
df.to_csv(path_or_buf='mefa_csv',index=False,encoding='cp949')