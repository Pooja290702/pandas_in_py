#to add elements into a file we use drop function
import pandas as pd
data = [
    {'Name':'Alice','Age':25},
    {'Name':'Bob','Age':30},
    {'Name':'Charlie','Age':35}
]

df = pd.DataFrame(data)
df['salary']=[100,200,300]     #adds a column salary
df=df.drop('salary',axis=1)       #drops/deletes a column salary
print(df)
