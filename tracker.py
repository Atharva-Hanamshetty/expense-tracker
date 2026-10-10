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
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return
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

def view_expenses(expenses):
    
    if not expenses:
        print("No expenses yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | {expense['category']} | {expense['amount']} | {expense['note']}"
        )

def delete_expense(expenses):
    
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid number.")
        return

    expenses.pop(number - 1)

    save_expenses(expenses)
    print("Deleted.")

def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()