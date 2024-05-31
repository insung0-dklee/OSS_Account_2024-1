import hashlib
import os
import json
from datetime import datetime
import pickle

# 전역 변수
userdata = {}
ledger = []
expenses_file = 'expenses.json'

# 회원가입 함수
def user_reg():
    id = input("id 입력: ")
    pw = input("password 입력: ")

    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    userdata[id] = pw_data

    with open('login.txt', 'a', encoding='UTF-8') as fw:
        for user_id, user_pw in userdata.items():
            fw.write(f'{user_id} : {user_pw}\n')

# 가계부 항목 추가 함수
def add_entry():
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    amount = float(input("금액: "))
    entry = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    ledger.append(entry)
    print("항목이 추가되었습니다.")

# 가계부 항목 조회 함수
def view_entries():
    for entry in ledger:
        print(entry)

# 월별 보고서 생성 함수
def generate_monthly_report():
    month = input("보고서 생성할 월 (YYYY-MM): ")
    monthly_total = 0
    for entry in ledger:
        if entry["date"].startswith(month):
            monthly_total += entry["amount"]
            print(entry)
    print(f"{month}월 총 지출: {monthly_total} 원")

# 예산 설정 및 초과 알림 함수
def set_budget():
    budget = float(input("예산 설정 (원): "))
    current_total = sum(entry["amount"] for entry in ledger)
    if current_total > budget:
        print(f"경고: 예산 초과! 현재 지출: {current_total} 원")
    else:
        print(f"예산 설정 완료. 현재 지출: {current_total} 원, 남은 예산: {budget - current_total} 원")

# 지출 카테고리 분석 함수
def analyze_categories():
    category_totals = {}
    for entry in ledger:
        category = entry["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += entry["amount"]
    for category, total in category_totals.items():
        print(f"{category}: {total} 원")

# 메모장 추가 함수
def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title, "w", encoding="utf8")
    print("내용 입력: ")
    str_memo = input()
    new_f.write(str_memo)
    new_f.close()

# 지출 내역 저장 함수
def save_expense(expense):
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    data.append(expense)
    with open(expenses_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 지출 내역 보기 함수
def view_expenses():
    with open(expenses_file, 'r') as file:
        data = json.load(file)
        if data:
            for idx, expense in enumerate(data, start=1):
                print(f"{idx}. {expense['date']} - {expense['item']} : {expense['amount']}원")
        else:
            print("저장된 지출 내역이 없습니다.")

# 지출 내역 입력 함수
def input_expense():
    date = input("지출 날짜 (예: 2024-05-30): ")
    item = input("지출 항목: ")
    amount = input("지출 금액: ")
    expense = {
        'date': date,
        'item': item,
        'amount': amount
    }
    save_expense(expense)
    print("지출 내역이 저장되었습니다.")

# 지출 내역 삭제 함수
def delete_expense():
    index = input("삭제할 지출 항목의 번호를 입력하세요: ")
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    try:
        index = int(index)
        if 1 <= index <= len(data):
            deleted_expense = data.pop(index - 1)
            with open(expenses_file, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                print(f"다음 내역이 삭제되었습니다: {deleted_expense}")
        else:
            print("잘못된 번호입니다. 다시 시도하세요.")
    except ValueError:
        print("숫자를 입력하세요.")

# 예상 지출 계산 함수
def predict_next_month_expense():
    total_expense = sum(entry["amount"] for entry in ledger if entry["amount"] < 0)
    months_count = len(set(entry["date"][:7] for entry in ledger))
    average_expense = total_expense / months_count if months_count > 0 else 0
    next_month_expense = average_expense
    print(f"다음 달 예상 지출: {next_month_expense} 원")

# 도움말 출력 함수
def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 월별 보고서 생성
    4: 예산 설정 및 초과 알림
    5: 지출 카테고리 분석
    6: 회원가입
    7: 예상 지출 항목
    ?: 도움말 출력
    exit: 종료
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        add_entry()
    elif func == "2":
        view_entries()
    elif func == "3":
        generate_monthly_report()
    elif func == "4":
        set_budget()
    elif func == "5":
        analyze_categories()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    elif func == "메모장":
        add_memo()
    elif func == "6":
        user_reg()
    elif func == "7":
        predict_next_month_expense()
    else:
        print("올바른 기능을 입력해 주세요.")

