import json
import os
import random
from datetime import datetime

# 가계부 데이터 파일 경로
expenses_file = 'expenses.json'
fixed_expenses_file = 'fixed_expenses.json'
points_file = "points.json"
expense_limit_file = "daily_limit.json"

# 포인트를 파일에서 불러오거나 초기화
def load_points():
    if os.path.exists(points_file):
        with open(points_file, "r") as file:
            return json.load(file).get("points", 0)
    return 0

points = load_points()

def save_points():
    with open(points_file, "w") as file:
        json.dump({"points": points}, file)

# 랜덤으로 도전 과제를 선택하여 반환하는 함수
def assign_challenge():
    challenges = [
        ("오늘은 가계부에 3개 이상의 지출을 기록해 볼까요~", 10),
        ("오늘은 점심시간에 외식을 하지 말고 집에서 저녁을 해결해 보세요!", 15),
        ("오늘은 필요한 것만 사는 쇼핑을 해보자구요!", 20)
    ]
    today_challenge = random.choice(challenges)
    return today_challenge

# 도전 과제를 완료했을 때 포인트를 추가하고 메시지를 출력하는 함수
def complete_challenge(points_awarded):
    global points
    points += points_awarded
    save_points()
    print(f"도전과제 완료! 티끌 모아 태산~ {points_awarded} 포인트를 받았습니다.")
    print(f"현재 포인트: {points}점")

def get_points():
    return points

# 일일 지출 한도 설정 기능
def set_daily_limit():
    try:
        limit = float(input("일일 지출 한도를 설정하세요 (원): "))
        with open(expense_limit_file, 'w') as file:
            json.dump({"limit": limit}, file)
        print(f"일일 지출 한도가 {limit}원으로 설정되었습니다.")
    except ValueError:
        print("유효한 금액을 입력하세요.")

# daily_limit.json 파일에서 일일 지출 한도를 가져오는 함수
def get_daily_limit():
    if os.path.exists(expense_limit_file):
        with open(expense_limit_file, 'r') as file:
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

# 특정 기간 내 지출 분석 기능
def analyze_expenses_in_period():
    start_date = input("시작 날짜를 입력하세요 (예: 2024-05-01): ")
    end_date = input("종료 날짜를 입력하세요 (예: 2024-05-31): ")

    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("올바른 날짜 형식을 입력하세요 (YYYY-MM-DD).")
        return

    total_expense = 0
    category_totals = {}
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            expense_date_obj = datetime.strptime(expense['date'], "%Y-%m-%d")
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

# 지출 패턴 예측 기능
def predict_future_expenses():
    days = int(input("몇 일 후까지의 지출을 예측하시겠습니까? (예: 30): "))
    total_expense = 0
    days_count = 0

    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for expense in data:
            total_expense += float(expense['amount'])
            days_count += 1

    if days_count == 0:
        print("지출 내역이 없습니다.")
        return

    daily_average_expense = total_expense / days_count
    future_expense = daily_average_expense * days
    print(f"예상 일일 평균 지출: {daily_average_expense:.2f} 원")
    print(f"{days}일 후 예상 총 지출: {future_expense:.2f} 원")

# 고정 지출 관리 기능
def add_fixed_expense():
    try:
        item = input("고정 지출 항목을 입력하세요: ")
        amount = float(input("고정 지출 금액을 입력하세요 (원): "))

        if not os.path.exists(fixed_expenses_file):
            with open(fixed_expenses_file, 'w') as file:
                json.dump([], file)

        with open(fixed_expenses_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append({"item": item, "amount": amount})
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"고정 지출 항목 '{item}'이(가) {amount}원으로 추가되었습니다.")
    except ValueError:
        print("유효한 금액을 입력하세요.")

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

if __name__ == "__main__":
    # 일일 지출 한도 설정
    set_daily_limit()

    # 현재 일일 지출 한도 확인
    limit = get_daily_limit()
    if limit is not None:
        print(f"현재 설정된 일일 지출 한도는 {limit}원입니다.")
    else:
        print("일일 지출 한도가 설정되지 않았습니다.")

    # 도전 과제 수행
    today_challenge, points_awarded = assign_challenge()
    print(today_challenge)

    user_input = input("이 도전과제를 완료했나요? (y/n): ").strip().lower()
    if user_input == "y":
        complete_challenge(points_awarded)
    else:
        print("도전과제를 완료하지 못했군요. 내일 다시 도전해보세요!")

    print(f"현재 포인트: {get_points()}점")

    # 일일 지출 한도 초과 여부 확인
    check_daily_limit()

    # 특정 기간 내 지출 분석
    analyze_expenses_in_period()

    # 지출 패턴 예측
    predict_future_expenses()

    # 고정 지출 관리
    add_fixed_expense()
    view_fixed_expenses()
    apply_fixed_expenses()
