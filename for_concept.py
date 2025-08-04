import pandas as pd

df=pd.read_csv("expenses.csv")
df.loc[1,"Amount"]=99999
print(df)
print(df.loc[1],)


# print(df.loc[:,'Amount'])