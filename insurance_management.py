import json
from datetime import datetime

insurance_file = 'insurance.json'

# 보험 데이터를 파일에 저장하는 함수
def save_insurance_data(data):
    with open(insurance_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 보험 데이터를 파일에서 불러오는 함수
def load_insurance_data():
    try:
        with open(insurance_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# 보험 계약 추가 함수
def add_insurance():
    company = input("보험사 이름: ")
    policy_number = input("보험 증권 번호: ")
    start_date = input("시작 일자 (YYYY-MM-DD): ")
    end_date = input("종료 일자 (YYYY-MM-DD): ")
    premium = float(input("보험료: "))

    new_policy = {
        "company": company,
        "policy_number": policy_number,
        "start_date": start_date,
        "end_date": end_date,
        "premium": premium
    }

    data = load_insurance_data()
    data.append(new_policy)
    save_insurance_data(data)
    print("보험 계약이 추가되었습니다.")

# 보험 계약 조회 함수
def view_insurance():
    data = load_insurance_data()
    if not data:
        print("등록된 보험 계약이 없습니다.")
    else:
        for idx, policy in enumerate(data, start=1):
            print(f"{idx}. 보험사: {policy['company']}, 증권 번호: {policy['policy_number']}, 시작 일자: {policy['start_date']}, 종료 일자: {policy['end_date']}, 보험료: {policy['premium']}원")

# 보험 계약 삭제 함수
def delete_insurance():
    view_insurance()
    data = load_insurance_data()
    if not data:
        return

    index = int(input("삭제할 보험 계약의 번호를 입력하세요: ")) - 1
    if 0 <= index < len(data):
        deleted_policy = data.pop(index)
        save_insurance_data(data)
        print(f"다음 보험 계약이 삭제되었습니다: {deleted_policy}")
    else:
        print("잘못된 번호입니다.")
