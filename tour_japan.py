import matplotlib.pyplot as plt
import pandas
import matplotlib.pyplot

df =pandas.read_csv('japan.csv')
year_2023 = df[(df['Year']==2023) & (df['Purpose_of_visit_to_Japan']=='Tourism')]
data = year_2023.groupby('Country/Area')['Visitor Arrivals'].sum()

