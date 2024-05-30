import matplotlib.pyplot as plt
import pandas

# x : age
# y : salary
df = pandas.read_csv("company.csv",encoding='cp949')

# salary = df['salary'].value_counts()
# salary.plot.pie()
# plt.show()

# job_satisfaction = df['job_satisfaction'].value_counts()
# job_satisfaction.plot.pie()
# plt.show()

x = df['age']
y = df['salary']

plt.hist2d(x,y)
plt.show()