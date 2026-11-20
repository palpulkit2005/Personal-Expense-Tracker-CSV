
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


def add_expense():
    print("\n===== ADD NEW EXPENSE =====")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    category = input("Enter category (Food/Travel/Shopping etc.): ").strip()

    if not category:
        print("Category cannot be empty!")
        return

    description = input("Enter description: ").strip()
    
    date_input = input("Enter expense date (YYYY-MM-DD) or press Enter for today: ").strip()

    if date_input:
        try:
            expense_date = date.fromisoformat(date_input).isoformat()
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")
            return
    else:
        expense_date = date.today().isoformat()


    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Amount", "Category", "Description"])

        writer.writerow([expense_date, amount, category, description])

    print("\nExpense added successfully!")

def view_expenses():
    print("\n===== ALL EXPENSES =====")

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet!")
        return

    print("-" * 65)
    print(f"{'Date':<15} {'Amount':<12} {'Category':<15} {'Description'}")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['Date']:<15} "
            f"₹{float(expense['Amount']):<11.2f} "
            f"{expense['Category']:<15} "
            f"{expense['Description']}"
        )

    print("-" * 65)


def total_expenses():
    print("\n===== TOTAL EXPENSES =====")

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    total = 0

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print(f"\nYour Total Expenses: ₹{total:.2f}")


def category_summary():
    print("\n===== CATEGORY-WISE SUMMARY =====")

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    category_totals = {}

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"].strip().title()
            amount = float(expense["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if not category_totals:
        print("No expenses recorded yet!")
        return

    for category, total in category_totals.items():
        print(f"{category:<15}: ₹{total:.2f}")



def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
