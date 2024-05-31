import hashlib
import os
import json
from datetime import datetime
import pickle

userdata = {}

def user_reg():  # 회원가입
    id = input("id 입력: ")
    pw = input("password 입력: ")

    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    userdata[id] = pw_data

    with open('login.txt', 'a', encoding='UTF-8') as fw:
        for user_id, user_pw in userdata.items():
            fw.write(f'{user_id} : {user_pw}\n')

def day_spending(hist, spending, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:
        hist[f"{dt}"] = []
    hist[f"{dt}"].append((-spending, where))

def day_income(hist, income, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:
        hist[f"{dt}"] = []
    hist[f"{dt}"].append((income, where))

def new_account(user_id, bal):
    household_ledger = {'user_id': user_id, 'bal': bal, 'history': {}}
    with open(f'{user_id}.txt', 'wb') as info:
        pickle.dump(household_ledger, info)

def open_account_info(user_id):
    try:
        with open(f'{user_id}.txt', 'rb') as info:
            user_dict = pickle.load(info)
        return user_dict
    except Exception as e:
        print(f"{user_id}의 정보를 불러오는 과정에서 오류가 발생하였습니다. : {e}")
        return None

def calculator():
    try:
        expr = input("계산할 수식을 입력하세요 (예: 2 + 3 * 4): ")
        result = eval(expr)
        print(f"결과: {result}")
    except Exception as e:
        print(f"오류 발생: {e}")

ledger = []

def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 월별 보고서 생성
    4: 예산 설정 및 초과 알림
    5: 지출 카테고리 분석
    6. 회원가입
    ?: 도움말 출력
    exit: 종료
    """)

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

def view_entries():
    for entry in ledger:
        print(entry)

def generate_monthly_report():
    month = input("보고서 생성할 월 (YYYY-MM): ")
    monthly_total = 0
    for entry in ledger:
        if entry["date"].startswith(month):
            monthly_total += entry["amount"]
            print(entry)
    print(f"{month}월 총 지출: {monthly_total} 원")

def set_budget():
    budget = float(input("예산 설정 (원): "))
    current_total = sum(entry["amount"] for entry in ledger)
    if current_total > budget:
        print(f"경고: 예산 초과! 현재 지출: {current_total} 원")
    else:
        print(f"예산 설정 완료. 현재 지출: {current_total} 원, 남은 예산: {budget - current_total} 원")

def analyze_categories():
    category_totals = {}
    for entry in ledger:
        category = entry["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += entry["amount"]
    for category, total in category_totals.items():
        print(f"{category}: {total} 원")

def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title, "w", encoding="utf8")
    print("내용 입력: ")
    str_memo = input()
    new_f.write(str_memo)
    new_f.close()

expenses_file = 'expenses.json'

if not os.path.exists(expenses_file):
    with open(expenses_file, 'w') as file:
        json.dump([], file)

def save_expense(expense):
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    data.append(expense)
    with open(expenses_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def view_expenses():
    with open(expenses_file, 'r') as file:
        data = json.load(file)
        if data:
            for idx, expense in enumerate(data, start=1):
                print(f"{idx}. {expense['date']} - {expense['item']} : {expense['amount']}원")
        else:
            print("저장된 지출 내역이 없습니다.")

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

b_is_exit = False

while not b_is_exit:
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
        b_is_exit = True
    elif func == "메모장":
        add_memo()
    elif func == "6":  # 회원가입 기능 추가
        user_reg()      # 사용자가 회원가입할 수 있도록 함수 호출
    else:
        print("올바른 기능을 입력해 주세요.")


