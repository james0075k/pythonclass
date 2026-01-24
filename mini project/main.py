#expenses tracker project
expenses = [] #list of expenses
print("Welcome to the Expenses Tracker!")

while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        expenses.append({'amount': amount, 'description': description})
        print("Expense added successfully!")
    
    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. {expense['description']}: ${expense['amount']:.2f}")
    
    elif choice == '3':
        if not expenses:
            print("No expenses to delete.")
        else:
            print("\nExpenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. {expense['description']}: ${expense['amount']:.2f}")
            to_delete = int(input("Enter the number of the expense to delete: "))
            if 1 <= to_delete <= len(expenses):
                deleted_expense = expenses.pop(to_delete - 1)
                print(f"Deleted expense: {deleted_expense['description']}: ${deleted_expense['amount']:.2f}")
            else:
                print("Invalid selection.")
    
    elif choice == '4':
        print("Exiting Expenses Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
