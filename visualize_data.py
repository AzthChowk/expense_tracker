import pandas as pd
import matplotlib.pyplot as plt

from categories import valid_categories
# category_length = len(valid_categories)
# print(category_length)
# summary_data = [0 for i in range(category_length)]
# summary_data[5] = 600
# print(summary_data)

# valid_categories.sort()


 


def visualize_bar(expenses,category_summary):
    print("Bar Chart")
    # Create bar plot
    plt.bar(valid_categories, category_summary)
    
    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Simple Bar Plot')
    
    # # Show plot
    plt.show()
def visualize_pie(category_summary):
    print("Pie Chart")
    plt.pie(category_summary, labels=valid_categories, autopct='%1.1f%%')
    plt.show() 

def visualize_data(expenses):
    df = pd.DataFrame(expenses)

    df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce')  # Convert to numeric
    total_expenses = df["Amount"].sum() # DataFrame Function to all the values - sum()
    # by default the groupby() sort in alphabetcial order - so to display as your desire - change sort = False
    category_summary = df.groupby(["Category"], sort=False)["Amount"].sum() # Dataframe Function - groupby()

    while True:
        print("Visualize data")
        print("\t5.1 Bar Chart ")
        print("\t5.2 Pie Chart ")
        break
    choice = input("Enter the choice : ")
    if choice == ("a"):

        visualize_bar(expenses, category_summary)
        
    elif choice ==("b"):
  
        visualize_pie(category_summary)
        
    else:
        print("Invalid option")
        
