import pandas as pd
import matplotlib.pyplot as plt

from categories import valid_categories
# category_length = len(valid_categories)
# print(category_length)
# summary_data = [0 for i in range(category_length)]
# summary_data[5] = 600
# print(summary_data)

# valid_categories.sort()

def visualize_summary(category_summary):
 
    # Create bar plot
    plt.bar(valid_categories, category_summary)
    
    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Simple Bar Plot')
    
    # # Show plot
    plt.show()


def view_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    df = pd.DataFrame(expenses)

    try:
        df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce')  # Convert to numeric
        total_expenses = df["Amount"].sum() # DataFrame Function to all the values - sum()
        print("\nTotal Expenses: ",total_expenses)
        # by default the groupby() sort in alphabetcial order - so to display as your desire - change sort = False
        category_summary = df.groupby(["Category"], sort=False)["Amount"].sum() # Dataframe Function - groupby()
        print("\nCategory-wise Summary:")
        print(category_summary)
        visualize_summary(category_summary)
  

    except Exception as e:
        print(f"Error calculating summary: {e}")


