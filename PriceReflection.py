import json
from datetime import datetime

# 물가 반영 데이터를 저장할 파일 이름
inflation_file = 'inflation_data.json'

def save_inflation_rate(year, rate):
    """연도별 물가 상승률을 저장합니다."""
    if not rate >= 0:
        print("물가 상승률은 0 이상이어야 합니다.")
        return
    
    # 기존 데이터를 불러옵니다.
    data = load_inflation_data()
    
    # 새 데이터를 추가합니다.
    data[year] = rate
    
    # 파일에 저장합니다.
    with open(inflation_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"{year}년 물가 상승률 {rate}%가 저장되었습니다.")

def load_inflation_data():
    """물가 상승률 데이터를 불러옵니다."""
    try:
        with open(inflation_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}
    
    return data

def apply_inflation(amount, from_year, to_year):
    """물가 상승률을 반영하여 금액을 계산합니다."""
    data = load_inflation_data()
    
    if from_year not in data or to_year not in data:
        print("해당 연도의 물가 상승률 데이터가 없습니다.")
        return amount
    
    if from_year >= to_year:
        print("목표 연도는 시작 연도보다 커야 합니다.")
        return amount
    
    adjusted_amount = amount
    for year in range(from_year, to_year):
        if str(year) in data:
            rate = data[str(year)]
            adjusted_amount *= (1 + rate / 100)
        else:
            print(f"{year}년의 물가 상승률 데이터가 없습니다.")
    
    return adjusted_amount

def get_inflation_adjusted_value():
    """사용자로부터 입력을 받아 물가 반영 금액을 계산합니다."""
    amount = float(input("금액을 입력하세요 (원): "))
    from_year = int(input("시작 연도를 입력하세요 (예: 2020): "))
    to_year = int(input("목표 연도를 입력하세요 (예: 2024): "))
    
    adjusted_amount = apply_inflation(amount, from_year, to_year)
    print(f"{from_year}년의 {amount}원은 {to_year}년의 {adjusted_amount:.2f}원과 같습니다.")
