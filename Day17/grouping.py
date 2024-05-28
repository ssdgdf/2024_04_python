import pandas

df = pandas.read_csv("company_csv",encoding='cp949')

group_department = df.groupby('department')
print(group_department.count())
print(group_department.value_counts())


group_age = df.groupby('age')
print(group_age.count())
print(group_department['age'].mean())
