# Expense Tracker

A command-line app to track your daily spending. Add expenses, view them, delete mistakes, and see totals by category. Data is saved to a JSON file, so it persists between runs.

## Features
- Add an expense with an amount, category, and note (date is added automatically)
- View all expenses in a numbered list
- Delete an expense by its number
- See totals per category and overall
- Input validation, so typing text instead of a number won't crash the app

## Tech
- Python 3
- Standard library only (`json`, `os`, `datetime`)

## How to run
```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker.git
cd expense-tracker
py tracker.py
```
(Use `python3 tracker.py` on Mac/Linux.)

## Example
```
1. Add expense
2. View all expenses
3. Delete an expense
4. Show totals by category
5. Quit
Choose an option: 2
1. 2026-10-11 | food | 1500.0 | dinner
2. 2026-10-11 | clothing | 300.0 | bata
```

## What I learned
- Reading and writing JSON files
- Using dictionaries to group and total data
- Handling errors with `try` / `except`
- Structuring a program into small functions

## Future improvements
- Filter expenses by date or month
- Edit an existing expense
- Export to CSV
