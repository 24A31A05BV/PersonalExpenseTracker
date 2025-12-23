import os

FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = input("Enter amount: ")
    note = input("Enter note (optional): ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")

    print("✅ Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("❌ No expenses recorded yet.\n")
        return

    print("\n--- Expense Records ---")
    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, note = line.strip().split(",")
            total += float(amount)
            print(f"Date: {date} | Category: {category} | Amount: ₹{amount} | Note: {note}")
    print(f"\n💰 Total Expense: ₹{total}\n")

def main():
    while True:
        print("==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

main()
