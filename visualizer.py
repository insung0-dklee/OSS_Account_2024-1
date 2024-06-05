import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

# 가계부 데이터 파일 경로
expenses_file = 'expenses.json'

# 지출 내역 로드 함수
def load_expenses():
    if os.path.exists(expenses_file):
        with open(expenses_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# 특정 기간의 지출 내역 시각화 함수
def visualize_expenses(start_date, end_date):
    expenses = load_expenses()
    if not expenses:
        print("저장된 지출 내역이 없습니다.")
        return

    dates = []
    amounts = []

    for expense in expenses:
        date = datetime.strptime(expense['date'], "%Y-%m-%d")
        if start_date <= date <= end_date:
            dates.append(date)
            amounts.append(float(expense['amount']))

    if not dates:
        print("해당 기간 내역이 없습니다.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Amount (원)')
    plt.title('Expense Over Time')
    plt.grid(True)
    plt.show()

# 지출 내역 카테고리별 시각화 함수
def visualize_income_expense():
    expenses = load_expenses()
    if not expenses:
        print("저장된 지출 내역이 없습니다.")
        return

    categories = {}
    for expense in expenses:
        category = expense['item']
        amount = float(expense['amount'])
        if category not in categories:
            categories[category] = 0
        categories[category] += amount

    labels = categories.keys()
    sizes = categories.values()

    plt.figure(figsize=(10, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Expenses by Category')
    plt.show()

# 예산 대비 실제 지출 시각화 함수
def visualize_budget():
    expenses = load_expenses()
    if not expenses:
        print("저장된 지출 내역이 없습니다.")
        return

    total_expense = sum(float(expense['amount']) for expense in expenses)
    budget = 0
    if os.path.exists('budget.json'):
        with open('budget.json', 'r', encoding='utf-8') as file:
            budget = json.load(file).get('budget', 0)

    labels = ['Budget', 'Spent']
    sizes = [budget, total_expense]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, sizes, color=['green', 'red'])
    plt.title('Budget vs. Actual Spending')
    plt.ylabel('Amount (원)')
    plt.show()