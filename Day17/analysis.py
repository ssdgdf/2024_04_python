import pandas


df = pandas.read_csv("company_csv",encoding='cp949')
# print(df[['name','salary','age']])
# print(df[df['salary']>=7000])
# print(df[df['year_at_company']>=7])

# a = df['performance_score']>=80
# b = df['year_at_company']>=10
# c = df['job_satisfaction']>=8
# print(df[a&b&c])


# 열 추가
# 5년이하 사원  10년이하 과장  15년이하 부장
# df['test'] = df['age'] =df['year_at_company']
# print(df)
def makerank(x):
    if x<=5:
        return "사원"
    elif x<=10:
        return "과장"
    else:
        return "부장"

#apply 함수
df['rank'] = df['year_at_company'].apply(makerank)
# performance_score 20점 권고사직 50점 직급유지 80점 보너스 100점 승진
def performance_rank(x):
    if x<=20:
        return "권고사직"
    elif x<=50:
        return "직급유지"
    elif x<=80:
        return "보너스"
    else:
        return "승진"
df['performance_rank'] = df['performance_score'].apply(performance_rank)
print(df)