import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def visualize_bar(expenses):
    # converting to Dataframe
    df= pd.DataFrame(expenses)
    # converting amount to numerical value
    df['Amount'] = pd.to_numeric(df["Amount"],errors='coerce')
    # grouping the data into its category
    df= df.groupby(["Category"], sort=False)["Amount"].sum().reset_index()
    # Draw Bar Graph
    print("Printing Bar Chart......")
    fig = px.bar(df, x='Category', y='Amount', title = "Category-wise expenses", labels={'Amount':"Total Amount",'Category':"Expense categories"}, color = "Category")
    fig.show()

def visualize_pie(expenses):
    df = pd.DataFrame(expenses)
    df['Amount'] = pd.to_numeric(df["Amount"],errors='coerce')
    # grouping the data into its category
    df= df.groupby(["Category"], sort=False)["Amount"].sum().reset_index()
    print("Printing Pie Chart......")
    fig = px.pie(df, values='Amount', names='Category', title='Category-wise expenses')
    fig.show()

# Scatter Plot
def visualize_scatter(expenses):
    df = pd.DataFrame(expenses)    
    fig = px.scatter(df, x="Date", y="Amount",color='Date', hover_data=['Title'])
    fig.show()

def visualize_data(expenses):
    while True:
        print("Visualize data")
        print("\ta Bar Chart ")
        print("\tb Pie Chart ")
        print("\tc Scatter Plot ")
        print("\td Area Plot ")
        break
    choice = input("Enter the choice : ")
    if choice == ("a"):
        visualize_bar(expenses)
        
    elif choice ==("b"):
        visualize_pie(expenses)
        
    elif choice ==("c"):
        visualize_scatter(expenses)
        
    else:
        print("Invalid option")
        
