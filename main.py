import json

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def filter_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def total_expense_by_month(self, year):
        total = 0
        for expense in self.expenses:
            if expense.name.startswith(str(year)):
                total += expense.amount
        return total

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump([{
                'name': expense.name,
                'amount': expense.amount,
                'category': expense.category
            } for expense in self.expenses], f)

# Misol
tracker = ExpenseTracker()

expense1 = Expense('2024-01-01', 100, 'Food')
expense2 = Expense('2024-01-15', 200, 'Food')
expense3 = Expense('2024-02-01', 300, 'Transport')

tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

print(tracker.filter_by_category('Food'))  # ['Food', 100, 200]
print(tracker.total_expense_by_month(2024))  # 300
tracker.save_to_json('expenses.json')
