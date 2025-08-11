import pandas as pd

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
        # Dataframe Function - groupby() & .reset_index() - in this case without it - Category is made index. with it - Category considered as column
        category_summary = df.groupby(["Category"])["Amount"].sum().reset_index() 
        print("\nCategory-wise Summary: \n")
        print(category_summary)
 
    except Exception as e:
        print(f"Error calculating summary: {e}")

