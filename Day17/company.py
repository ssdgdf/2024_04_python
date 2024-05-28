import pandas
from faker import Faker
import random
f = Faker('ko_KR')
agelist = ["20대","30대","40대","50대","60대"]
salaryList = [3000+ x*500 for x in range(14)]
depList = ["영업부","사업부","개발부","경영부","인사부","생산부"]

data = {
    'name':[f.name()  for x in range(300)],
    'age':[random.choice(agelist) for x in range(300)],
    'salary':[random.choice(salaryList) for x in range(300)],
    'department':[random.choice(depList) for x in range(300)],
    'year_at_company':[random.randint(1,15) for x in range(300)],
    'job_satisfaction':[random.randint(1,10) for x in range(300)],
    'performance_score':[random.randint(1,100) for x in range(300)]
}

df =pandas.DataFrame(data)
df.to_csv(path_or_buf='company_csv',index=False,encoding='cp949')