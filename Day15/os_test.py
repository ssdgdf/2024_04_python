import os
import datetime
from review import yearTozodiac
print(os.getlogin())

# 바탕화면 경로 따기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')

# 바탕화면경로와 폴더이름 합치기
folder_path = os.path.join(desktop_path,'과장님_부당업무_지시_폴더')

# 폴더 만들기
os.mkdir(folder_path)

# 오늘 날짜 가져오기
start_date = datetime.date.today()

# 폴더:용띠의해_5월_23일_목요일



for x in range(365):
    date_folder = start_date+datetime.timedelta(days=x)
    year_zodiac = yearTozodiac(int(date_folder.strftime("%Y")))
    folder_name = f"{year_zodiac}띠의 해{date_folder.strftime("%m-%d_%A")}"
    path = os.path.join(folder_path, folder_name)
    os.mkdir(path)



