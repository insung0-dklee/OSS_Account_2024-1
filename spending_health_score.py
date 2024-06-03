# spending_health_score.py
import json
from datetime import datetime

expenses_file = 'expenses.json'

def calculate_spending_health_score():
    expenses = load_expenses()
    if not expenses:
        print("저장된 지출 내역이 없습니다.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense["item"]
        amount = float(expense["amount"])
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount

    total_expense = sum(category_totals.values())
    score = 100

    advice = []
    for category, total in category_totals.items():
        percentage = (total / total_expense) * 100
        if percentage > 30:
            score -= 10
            advice.append(f"{category}에서 지출이 총 지출의 {percentage:.2f}%를 차지합니다. {category}에서 절약할 수 있는 방법을 찾아보세요.")
        elif percentage > 20:
            score -= 5
            advice.append(f"{category}에서 지출이 총 지출의 {percentage:.2f}%를 차지합니다. 조금 더 신경 써서 지출을 줄여보세요.")
    
    print(f"지출 건강 점수: {score}점")
    if advice:
        print("지출을 줄일 수 있는 조언:")
        for a in advice:
            print(a)
    else:
        print("지출이 잘 관리되고 있습니다!")

def load_expenses():
    try:
        with open(expenses_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"지출 내역을 불러오는 중 오류가 발생했습니다: {e}")
        return []
