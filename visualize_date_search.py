import pandas as pd
from datetime import datetime
import plotly.express as px


def visualize_search_expense(expenses):
    while True:
        try:
            start_date = input("Enter start date (YYYY-MM-DD):")
            valid_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            break
        except:
            print("Enter valid start date")
    while True:
        try:
            end_date = input("Enter end date (YYYY-MM-DD):")
            valid_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            break
        except:
            print("Enter valid end date")

    df = pd.DataFrame(expenses)
    filter_list = df[(df["Date"] >= start_date) &(df["Date"] <= end_date)]
    if filter_list.empty:
        print("Sorry, No record/s found.")
    else:
        fig = px.scatter(filter_list, x="Date", y="Amount",color='Date', hover_data=['Description'])
        fig.show()
        # print(filter_list)

