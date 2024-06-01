import json
import os
from datetime import datetime

# 환경 영향 데이터를 정의 (간단한 예시 데이터)
carbon_footprint_data = {
    "식품": 5.0,  # kg CO2e per unit
    "교통": 20.0,
    "의류": 10.0,
    "에너지": 15.0,
    "기타": 8.0
}

# 지출 파일 초기화
expenses_file = 'expenses.json'
if not os.path.exists(expenses_file):
    with open(expenses_file, 'w') as file:
        json.dump([], file)

# 지출 내역 저장 함수
def save_expense(expense):
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    data.append(expense)
    with open(expenses_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 환경 영향 계산 함수
def calculate_environmental_impact(category, amount):
    if category in carbon_footprint_data:
        return carbon_footprint_data[category] * amount
    else:
        return carbon_footprint_data["기타"] * amount

# 지출 내역 입력 함수 (환경 영향 계산 추가)
def input_expense():
    date = input("지출 날짜 (예: 2024-05-30): ")
    item = input("지출 항목: ")
    amount = float(input("지출 금액: "))
    category = input("카테고리 (식품, 교통, 의류, 에너지, 기타): ")
    carbon_footprint = calculate_environmental_impact(category, amount)
    expense = {
        'date': date,
        'item': item,
        'amount': amount,
        'category': category,
        'carbon_footprint': carbon_footprint
    }
    save_expense(expense)
    print(f"지출 내역이 저장되었습니다. 예상 탄소 배출량: {carbon_footprint:.2f} kg CO2e")

# 지출 내역 보기 함수 (환경 영향 포함)
def view_expenses():
    with open(expenses_file, 'r') as file:
        data = json.load(file)
        if data:
            for idx, expense in enumerate(data, start=1):
                print(f"{idx}. {expense['date']} - {expense['item']} : {expense['amount']}원, 탄소 배출량: {expense['carbon_footprint']:.2f} kg CO2e")
        else:
            print("저장된 지출 내역이 없습니다.")

# 누적 탄소 배출량 계산 함수
def calculate_total_carbon_footprint():
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    total_carbon_footprint = sum(expense['carbon_footprint'] for expense in data)
    print(f"총 누적 탄소 배출량: {total_carbon_footprint:.2f} kg CO2e")

# 도움말 출력 함수
def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 총 누적 탄소 배출량 조회
    ?: 도움말 출력
    exit: 종료
    """)

