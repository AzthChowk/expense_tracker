import pandas as pd
from datetime import datetime
import os
import matplotlib

CSV_FILE = "expenses.csv"

def load_expenses(filename=CSV_FILE):
    if os.path.exists(filename):
        return pd.read_csv(filename).to_dict(orient="records")
    else:
        return []
# save the input to csv format - previously, saved as json format
def save_expenses(expenses, filename=CSV_FILE):
    df = pd.DataFrame(expenses)
    df.to_csv(filename, index=False)

def add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount, exp_description):
    datetime.strptime(exp_date, "%Y-%m-%d")  # Validate date format
    expense = {
        "Id": len(expenses) + 1,
        "Date": exp_date,
        "Category": exp_category,
        "Title": exp_title,
        "Amount": exp_amount,
        "Description": exp_description
    }
    expenses.append(expense)

def print_expense_list(expenses):
    df = pd.DataFrame(expenses)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

def view_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    df = pd.DataFrame(expenses)

    try:
        df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce')  # Convert to numeric
        total_expenses = df["Amount"].sum() # DataFrame Function to all the values - sum()
        print("\nTotal Expenses: ",total_expenses)

        category_summary = df.groupby("Category")["Amount"].sum() # Dataframe Function - groupby()
        print("\nCategory-wise Summary:")
        print(category_summary)
  


    except Exception as e:
        print(f"Error calculating summary: {e}")


def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker\n1. Add expense \n2. View expenses \n3. View Summary \n4. Exit")
        choice = input("Enter choice : ")

        if choice == "1":
            exp_date = input("Enter date (YYYY-MM-DD): ")
            exp_category = input("Enter expense category.\n Food, Transportation, Lifestyle, Health, Housing, Entertainment, Savinga and Payment, Pets, Education, Other : ").lower()
            exp_title = input("Enter expense title: ")
            exp_amount = float(input("Enter the amount: "))
            exp_description = input("Enter the description: ")

            add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount, exp_description)
            save_expenses(expenses)
            print("Expense added successfully.")

        elif choice == "2":
            print_expense_list(expenses)

        elif choice == "3":
            view_summary(expenses)


        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
main()
