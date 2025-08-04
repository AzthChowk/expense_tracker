import pandas as pd
from datetime import datetime
import os
import uuid
import matplotlib.pyplot as plt
from view_summary import view_summary
from categories import *


current_time = datetime.now()

CSV_FILE = "expenses_list.csv"

# Load the file; if not found, creates a empty list
def load_expenses(filename=CSV_FILE):
    if os.path.exists(filename):
        return pd.read_csv(filename).to_dict(orient="records")
    else:
        return []
    
# save the input to csv format - previously, saved as json format
def save_expenses(expenses, filename=CSV_FILE):
    df = pd.DataFrame(expenses)
    df.to_csv(filename, index=False)

# add the input to the file
def add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount,exp_payment, exp_description):
    datetime.strptime(exp_date, "%Y-%m-%d")  # Validate date format
    expense = {
        "Id": uuid.uuid4(),
        "Date": exp_date,
        "Category": exp_category,
        "Title": exp_title,
        "Amount": exp_amount,
        "Payment method": exp_payment,
        "Description": exp_description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def print_expense_list(expenses):
    df = pd.DataFrame(expenses)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)



def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker\n1. Add Expense \n2. View Expense list \n3. Update Expense \n4. Delete Expense \n5. View Summary \n6. Exit \n")
        choice = input("Enter choice : ")

        if choice == "1":
            while True:
                try:
                    exp_date = input("Enter a date (YYYY-MM-DD) : ")
                    valid_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
                    if current_time.date() > valid_date:
                        break
                except:
                    print("Invalid date, Check the date. Please enter in YYYY-MM-DD format.")

            while True:
                try:
                    exp_category = input("Enter expense category.\n Food, Transportation, Lifestyle, Health, Housing, Entertainment, Savings and Payment, Pets, Education, Other : ").lower()
                    if exp_category.strip().title() in valid_categories:
                        break
                except:
                    print("Enter the valid category")

            exp_title = input("Enter expense title : ")
            while True:
                try:
                    exp_amount = float(input("Enter the amount : "))
                    if exp_amount>0:
                        break
                except ValueError:
                    print("Enter proper amount")
            exp_payment = input("Mode of payment : ")
            exp_description = input("Enter the description : ")

            add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount, exp_payment, exp_description)
            save_expenses(expenses)

        elif choice == "2":
            print_expense_list(expenses)

        elif choice == "3":
            print('update section')

        elif choice == "4":
            print("delete section")
            break
        elif choice == "5":
            view_summary(expenses)
            
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")
main()


