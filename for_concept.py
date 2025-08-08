import random
import pandas as pd

# df=pd.read_csv("expenses.csv")
# df.loc[1,"Amount"]=99999
# print(df)
# print(df.loc[1],)

list = []

def data_entry():

    name = input("Enter name of the student : ")
    while True:
        try:
            score = float(input("Enter the total score : "))
            break
        except:
            print("Enter valid number : ")

    list.append({"name":name, "score":score})

data_entry()

print(list)

