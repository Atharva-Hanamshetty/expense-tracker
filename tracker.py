import json
import os
from datetime import date

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": str(date.today()),
    }

    expenses.append(expense)

    save_expenses(expenses)

expenses = load_expenses()
add_expense(expenses)
print(expenses)