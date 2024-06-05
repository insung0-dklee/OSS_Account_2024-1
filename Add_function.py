import json
import os
from datetime import datetime

# 가계부 데이터 파일 경로
expenses_file = 'expenses.json'
fixed_expenses_file = 'fixed_expenses.json'

# 1. 일일 지출 한도 설정 기능
# 사용자가 일일 지출 한도를 설정하도록 하는 함수
def set_daily_limit():
    try:
        # 사용자로부터 일일 지출 한도 입력 받기
        limit = float(input("일일 지출 한도를 설정하세요 (원): "))
        # daily_limit.json 파일에 한도 저장
        with open('daily_limit.json', 'w') as file:
            json.dump({"limit": limit}, file)
        print(f"일일 지출 한도가 {limit}원으로 설정되었습니다.")
    except ValueError:
        print("유효한 금액을 입력하세요.")

# daily_limit.json 파일에서 일일 지출 한도를 가져오는 함수
def get_daily_limit():
    if os.path.exists('daily_limit.json'):
        with open('daily_limit.json', 'r') as file:
            data = json.load(file)
        return data.get("limit", None)
    return None

# 오늘의 지출 금액이 일일 한도를 초과했는지 확인하는 함수
def check_daily_limit():
    limit = get_daily_limit()
    if limit is None:
        print("설정된 일일 지출 한도가 없습니다.")
        return

    total_spent_today = 0
    today = datetime.today().strftime('%Y-%m-%d')
    # expenses.json 파일에서 오늘의 지출 내역을 읽어옴
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            if expense['date'] == today:
                total_spent_today += float(expense['amount'])

    print(f"오늘 지출: {total_spent_today}원")
    if total_spent_today > limit:
        print(f"경고: 오늘의 지출이 한도를 초과했습니다! ({limit}원 초과)")
    else:
        print(f"남은 한도: {limit - total_spent_today}원")

# 2. 특정 기간 내 지출 분석 기능
# 사용자가 지정한 기간 내의 지출 내역을 분석하는 함수
def analyze_expenses_in_period():
    start_date = input("시작 날짜를 입력하세요 (예: 2024-05-01): ")
    end_date = input("종료 날짜를 입력하세요 (예: 2024-05-31): ")

    try:
        # 입력받은 날짜 문자열을 datetime 객체로 변환
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("올바른 날짜 형식을 입력하세요 (YYYY-MM-DD).")
        return

    total_expense = 0
    category_totals = {}
    # expenses.json 파일에서 지출 내역을 읽어옴
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            expense_date_obj = datetime.strptime(expense['date'], "%Y-%m-%d")
            # 지출 내역이 지정한 기간 내에 속하는지 확인
            if start_date_obj <= expense_date_obj <= end_date_obj:
                amount = float(expense['amount'])
                total_expense += amount
                category = expense['item']
                if category not in category_totals:
                    category_totals[category] = 0
                category_totals[category] += amount

    print(f"{start_date}부터 {end_date}까지의 총 지출: {total_expense} 원")
    print("카테고리별 지출 내역:")
    for category, total in category_totals.items():
        print(f"{category}: {total} 원")

# 3. 지출 패턴 예측 기능
# 사용자가 지정한 일 수 이후의 예상 지출을 예측하는 함수
def predict_future_expenses():
    days = int(input("몇 일 후까지의 지출을 예측하시겠습니까? (예: 30): "))
    total_expense = 0
    days_count = 0

    # expenses.json 파일에서 지출 내역을 읽어옴
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            total_expense += float(expense['amount'])
            days_count += 1

    if days_count == 0:
        print("지출 내역이 없습니다.")
        return

    # 일일 평균 지출 계산
    daily_average_expense = total_expense / days_count
    # 지정한 일 수 동안의 예상 지출 계산
    future_expense = daily_average_expense * days
    print(f"예상 일일 평균 지출: {daily_average_expense:.2f} 원")
    print(f"{days}일 후 예상 총 지출: {future_expense:.2f} 원")

# 4. 고정 지출 관리 기능
# 고정 지출 추가 함수
def add_fixed_expense():
    try:
        # 사용자로부터 고정 지출 항목과 금액 입력 받기
        item = input("고정 지출 항목을 입력하세요: ")
        amount = float(input("고정 지출 금액을 입력하세요 (원): "))

        # 고정 지출 내역을 저장할 파일이 있는지 확인하고, 없으면 생성
        if not os.path.exists(fixed_expenses_file):
            with open(fixed_expenses_file, 'w') as file:
                json.dump([], file)

        # 고정 지출 내역을 파일에 저장
        with open(fixed_expenses_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append({"item": item, "amount": amount})
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"고정 지출 항목 '{item}'이(가) {amount}원으로 추가되었습니다.")
    except ValueError:
        print("유효한 금액을 입력하세요.")

# 고정 지출 조회 함수
def view_fixed_expenses():
    if os.path.exists(fixed_expenses_file):
        with open(fixed_expenses_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data:
                print("고정 지출 내역:")
                for idx, expense in enumerate(data, start=1):
                    print(f"{idx}. 항목: {expense['item']}, 금액: {expense['amount']}원")
            else:
                print("고정 지출 내역이 없습니다.")
    else:
        print("고정 지출 내역이 없습니다.")

# 고정 지출 적용 함수
def apply_fixed_expenses():
    today = datetime.today().strftime('%Y-%m-%d')
    if os.path.exists(fixed_expenses_file):
        with open(fixed_expenses_file, 'r', encoding='utf-8') as file:
            fixed_expenses = json.load(file)
            if fixed_expenses:
                with open(expenses_file, 'r+', encoding='utf-8') as exp_file:
                    expenses = json.load(exp_file)
                    for fixed_expense in fixed_expenses:
                        expenses.append({
                            'date': today,
                            'item': fixed_expense['item'],
                            'amount': fixed_expense['amount']
                        })
                    exp_file.seek(0)
                    json.dump(expenses, exp_file, ensure_ascii=False, indent=4)
                print("고정 지출이 오늘의 지출 내역에 추가되었습니다.")
            else:
                print("적용할 고정 지출 내역이 없습니다.")
    else:
        print("적용할 고정 지출 내역이 없습니다.")