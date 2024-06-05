import json
from datetime import datetime, timedelta

# 여행에 대한 기본 정보를 저장하는 딕셔너리
trip_details = {}

# 여행 예산 세부 항목을 저장하는 딕셔너리
trip_budget = {}

# 여행 중 실제 지출 내역을 저장하는 리스트
trip_expenses = []

# 여행 메모 및 체크리스트를 저장하는 리스트
trip_checklist = []

def set_trip_details():
    """
    여행에 대한 기본 정보를 설정하는 함수
    """
    destination = input("여행지: ")
    start_date = input("시작 날짜 (YYYY-MM-DD): ")
    end_date = input("종료 날짜 (YYYY-MM-DD): ")

    trip_details["destination"] = destination
    trip_details["start_date"] = start_date
    trip_details["end_date"] = end_date

    print(f"여행 정보가 설정되었습니다: {trip_details}")

def set_trip_budget():
    """
    여행 예산 세부 항목을 설정하는 함수
    """
    print("여행 예산을 설정합니다.")
    while True:
        category = input("예산 항목 (종료: '끝'): ")
        if category == '끝':
            break
        amount = float(input(f"{category} 예산 금액: "))
        trip_budget[category] = amount

    print(f"여행 예산이 설정되었습니다: {trip_budget}")

def add_trip_expense():
    """
    여행 중 실제 지출 내역을 추가하는 함수
    """
    category = input("지출 항목: ")
    amount = float(input("지출 금액: "))

    trip_expenses.append({ "category": category, "amount": amount })
    print(f"지출 내역이 추가되었습니다: {trip_expenses[-1]}")

def view_trip_summary():
    """
    여행 예산과 실제 지출 내역을 비교하여 요약을 제공하는 함수
    """
    print("\n여행 예산 요약:")
    total_budget = sum(trip_budget.values())
    total_expense = sum(expense["amount"] for expense in trip_expenses)

    print(f"총 예산: {total_budget} 원")
    print(f"총 지출: {total_expense} 원")

    for category, budget in trip_budget.items():
        spent = sum(expense["amount"] for expense in trip_expenses if expense["category"] == category)
        print(f"{category}: 예산 {budget} 원, 지출 {spent} 원, 차이 {budget - spent} 원")

    if total_expense > total_budget:
        print("경고: 예산을 초과했습니다!")
    else:
        print("예산 내에서 지출하고 있습니다.")

def save_trip_data(filename):
    """
    여행 데이터를 JSON 파일로 저장하는 함수
    """
    trip_data = {
        "details": trip_details,
        "budget": trip_budget,
        "expenses": trip_expenses,
        "checklist": trip_checklist
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(trip_data, f, ensure_ascii=False, indent=4)
    print(f"여행 데이터가 {filename} 파일로 저장되었습니다.")

def load_trip_data(filename):
    """
    JSON 파일에서 여행 데이터를 불러오는 함수
    """
    global trip_details, trip_budget, trip_expenses, trip_checklist
    with open(filename, 'r', encoding='utf-8') as f:
        trip_data = json.load(f)
        trip_details = trip_data["details"]
        trip_budget = trip_data["budget"]
        trip_expenses = trip_data["expenses"]
        trip_checklist = trip_data["checklist"]
    print(f"{filename} 파일에서 여행 데이터를 불러왔습니다.")

def add_checklist_item():
    """
    여행 메모 및 체크리스트 항목을 추가하는 함수
    """
    item = input("추가할 항목: ")
    trip_checklist.append(item)
    print(f"체크리스트에 항목이 추가되었습니다: {item}")

def view_checklist():
    """
    여행 메모 및 체크리스트를 조회하는 함수
    """
    print("\n여행 체크리스트:")
    for idx, item in enumerate(trip_checklist, start=1):
        print(f"{idx}. {item}")

def check_payments_due():
    """
    예산 초과 시 자동 알림을 제공하는 함수
    """
    total_budget = sum(trip_budget.values())
    total_expense = sum(expense["amount"] for expense in trip_expenses)

    if total_expense > total_budget:
        print("경고: 예산을 초과했습니다! 예산 초과 상태를 확인하세요.")

def generate_expense_report():
    """
    여행 경비 분석 리포트를 생성하는 함수
    """
    print("\n여행 경비 분석 리포트:")
    total_expense = sum(expense["amount"] for expense in trip_expenses)
    category_expenses = {}

    for expense in trip_expenses:
        category = expense["category"]
        if category not in category_expenses:
            category_expenses[category] = 0
        category_expenses[category] += expense["amount"]

    for category, amount in category_expenses.items():
        percentage = (amount / total_expense) * 100
        print(f"{category}: {amount} 원 ({percentage:.2f}%)")

def recommend_travel_destination():
    """
    예산과 선호도를 기반으로 여행지를 추천하는 함수
    """
    budget = float(input("여행 예산을 입력하세요: "))
    preferences = input("선호하는 활동 (예: 해변, 등산, 쇼핑 등): ")

    if budget < 1000000:
        if "해변" in preferences:
            print("추천 여행지: 동해안")
        elif "등산" in preferences:
            print("추천 여행지: 설악산")
        else:
            print("추천 여행지: 강원도")
    elif budget < 5000000:
        if "해변" in preferences:
            print("추천 여행지: 제주도")
        elif "등산" in preferences:
            print("추천 여행지: 지리산")
        else:
            print("추천 여행지: 서울")
    else:
        if "해변" in preferences:
            print("추천 여행지: 발리")
        elif "등산" in preferences:
            print("추천 여행지: 알프스")
        else:
            print("추천 여행지: 뉴욕")
