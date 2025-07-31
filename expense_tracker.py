import json
from datetime import datetime

import pandas as pd

    
def load_expenses(filename="list.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("list.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount, exp_description):
        datetime.strptime(exp_date, "%Y-%m-%d")
        expense = {
        "Id": len(expenses)+1,
        "Date": exp_date,
        "Category":exp_category,
        "Title":exp_title,
        "Amount":exp_amount,
        "Description":exp_description
        }
        expenses.append(expense)
def print_expense_list(expenses):
     df = pd.DataFrame(expenses)
     print(df)
    #  for expense in expenses:
    #       print(expense)

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker\n1. Add expense \n2. View expenses \n3. Delete expense \n4. Exit")
        choice = input("Enter choice : ")
        if choice == "1":
            exp_date = input("Enter date (YYYY-MM-DD): ")
            exp_category = input("Enter expense category.\n Food, Transportation, Lifestyle, Health, Housing, Entertainment, Savinga and Payment, Pets, Education, Other : ").lower()
            exp_title = input("Enter expense title : ")
            exp_amount = int(input("Enter the amount : "))
            exp_description = input("Enter the description : ")

            add_expenses(expenses, exp_date, exp_title, exp_category, exp_amount, exp_description)
            save_expenses(expenses)
            # prompt to add another item
            # while True:
            #     choice = input("Want to add another: Enter Yes/No")
            #     if (choice!="yes"):
            #         break
        elif choice =="2":
            print_expense_list(expenses)

        elif choice =="3":
            break
        else:
            break

    
main()
