import json
import os
from datetime import datetime

# 가계부 데이터 파일 경로
expenses_file = 'expenses.json'
daily_budget_file = 'daily_budget.json'

def set_daily_budget():
    try:
        budget = float(input("일일 예산을 설정하세요 (원): "))
        with open(daily_budget_file, 'w') as file:
            json.dump({"budget": budget}, file)
        print(f"일일 예산이 {budget}원으로 설정되었습니다.")
    except ValueError:
        print("유효한 금액을 입력하세요.")

def get_daily_budget():
    if os.path.exists(daily_budget_file):
        with open(daily_budget_file, 'r') as file:
            data = json.load(file)
        return data.get("budget", None)
    return None

def check_daily_budget():
    budget = get_daily_budget()
    if budget is None:
        print("설정된 일일 예산이 없습니다.")
        return

    total_spent_today = 0
    today = datetime.today().strftime('%Y-%m-%d')
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            if expense['date'] == today:
                total_spent_today += float(expense['amount'])

    print(f"오늘 지출: {total_spent_today}원")
    if total_spent_today > budget:
        print(f"경고: 오늘의 지출이 일일 예산을 초과했습니다! ({budget}원 초과)")
    else:
        print(f"남은 일일 예산: {budget - total_spent_today}원")
