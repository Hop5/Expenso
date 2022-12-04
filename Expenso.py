# define a dictionary to store your income and expenses
budget = {
    "income": [],
    "expenses": []
}

# define a function to add income or expenses to the budget
def add_transaction(transaction_type, amount, description):
    budget[transaction_type].append({
        "amount": amount,
        "description": description
    })

# define a function to print the budget
def print_budget():
    # calculate the total income and expenses
    total_income = sum([t["amount"] for t in budget["income"]])
    total_expenses = sum([t["amount"] for t in budget["expenses"]])

    # calculate the total savings
    total_savings = total_income - total_expenses

    # print the income, expenses, and savings
    print("Income: ", total_income)
    print("Expenses: ", total_expenses)
    print("Savings: ", total_savings)

    # print the individual income and expenses
    print("Income:")
    for transaction in budget["income"]:
        print(f"- {transaction['description']}: {transaction['amount']}")
    print("Expenses:")
    for transaction in budget["expenses"]:
        print(f"- {transaction['description']}: {transaction['amount']}")

# add some transactions to the budget
add_transaction("income", 1000, "Salary")
add_transaction("income", 500, "Freelance work")
add_transaction("expenses", 200, "Rent")
add_transaction("expenses", 100, "Groceries")

# print the budget
print_budget()
