import hashlib  # hashlib 사용
import os
import json
from datetime import datetime
import pickle

userdata = {}  # 아이디, 비밀번호 저장해둘 딕셔너리

def user_reg():  # 회원가입
    id = input("id 입력: ")  # 회원가입 시의 id 입력
    pw = input("password 입력: ")  # 회원가입 시의 pw 입력
    h = hashlib.sha256()  # hashlib 모듈의 sha256 사용
    h.update(pw.encode())  # sha256으로 암호화
    pw_data = h.hexdigest()  # 16진수로 변환

    userdata[id] = pw_data  # key에 id값을, value에 비밀번호 값

    with open('login.txt', 'a', encoding='UTF-8') as fw:  # utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items():  # 딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n')  # key, value값을 차례로 login.txt파일에 저장

def day_spending(hist, spending, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:  # 해당 일자에 수입지출 내역이 없을 시,
        hist[f"{dt}"] = []  # 새 리스트 생성
    hist[f"{dt}"].append((-spending, where))

def day_income(hist, income, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:  # 해당 일자에 수입지출 내역이 없을 시,
        hist[f"{dt}"] = []  # 새 리스트 생성
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

# 가계부 데이터 저장 변수
ledger = []

# 도움말 출력 함수
def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 월별 보고서 생성
    4: 예산 설정 및 초과 알림
    5: 지출 카테고리 분석
    6: 세금 및 보험 계산
    7: 계정 정보 조회
    8: 메모장
    ?: 도움말 출력
    exit: 종료
    """)

# 수입/지출 항목 추가 함수
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

# 항목 조회 함수
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

def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title, "w", encoding="utf8")
    print("내용 입력: ")
    str_memo = input()
    new_f.write(str_memo)
    new_f.close()

# 지출 내역을 저장할 파일 이름
expenses_file = 'expenses.json'

# 프로그램 시작 시 파일이 존재하지 않는 경우 초기화
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

# 근로소득세 계산 함수
def calculate_income_tax():
    income = float(input("총 소득을 입력하세요 (원): "))
    
    # 근로소득공제 계산
    if income <= 500000:
        deduction = income * 0.7
    elif income <= 15000000:
        deduction = 350000 + (income - 500000) * 0.4
    elif income <= 45000000:
        deduction = 5150000 + (income - 15000000) * 0.15
    elif income <= 100000000:
        deduction = 9150000 + (income - 45000000) * 0.05
    else:
        deduction = 9150000 + (income - 45000000) * 0.05
        deduction += (income - 100000000) * 0.02
        if deduction > 20000000:
            deduction = 20000000

    taxable_income = income - deduction

    # 기본 세율에 따른 세금 계산
    tax = 0
    if taxable_income <= 12000000:
        tax = taxable_income * 0.06
    elif taxable_income <= 46000000:
        tax = 12000000 * 0.06 + (taxable_income - 12000000) * 0.15
    elif taxable_income <= 88000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + (taxable_income - 46000000) * 0.24
    elif taxable_income <= 150000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + (taxable_income - 88000000) * 0.35
    elif taxable_income <= 300000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + (taxable_income - 150000000) * 0.38
    elif taxable_income <= 500000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + (taxable_income - 300000000) * 0.40
    elif taxable_income <= 1000000000:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + (taxable_income - 500000000) * 0.42
    else:
        tax = 12000000 * 0.06 + 34000000 * 0.15 + 42000000 * 0.24 + 62000000 * 0.35 + 150000000 * 0.38 + 200000000 * 0.40 + (taxable_income - 1000000000) * 0.45

    # 표준 세액 공제
    tax_credit = min(tax * 0.07, 740000)

    tax -= tax_credit

    print(f"총 소득: {income} 원")
    print(f"근로소득공제: {deduction} 원")
    print(f"과세 표준: {taxable_income} 원")
    print(f"세금 공제 전: {tax + tax_credit} 원")
    print(f"세금 공제 후: {tax} 원")

# 부가가치세 계산 함수
def calculate_vat():
    price_with_vat = float(input("부가가치세가 포함된 물품 가격을 입력하세요 (원): "))
    vat_rate = 0.1
    price_without_vat = price_with_vat / (1 + vat_rate)
    vat_amount = price_with_vat - price_without_vat

    print(f"부가가치세가 포함된 물품 가격: {price_with_vat} 원")
    print(f"부가가치세가 없는 원래 가격: {price_without_vat:.2f} 원")
    print(f"부가가치세: {vat_amount:.2f} 원")

# 4대 보험 계산 함수
def calculate_insurance():
    income = float(input("총 소득을 입력하세요 (원): "))
    national_pension_rate = 0.045
    health_insurance_rate = 0.03495
    long_term_care_rate = 0.1227
    employment_insurance_rate = 0.009

    national_pension = income * national_pension_rate
    health_insurance = income * health_insurance_rate
    long_term_care = health_insurance * long_term_care_rate
    employment_insurance = income * employment_insurance_rate

    total_insurance = national_pension + health_insurance + long_term_care + employment_insurance
    after_insurance_income = income - total_insurance

    print(f"총 소득: {income} 원")
    print(f"국민연금: {national_pension:.2f} 원")
    print(f"건강보험: {health_insurance:.2f} 원")
    print(f"장기요양보험: {long_term_care:.2f} 원")
    print(f"고용보험: {employment_insurance:.2f} 원")
    print(f"총 4대 보험료: {total_insurance:.2f} 원")
    print(f"4대 보험료 공제 후 금액: {after_insurance_income:.2f} 원")

# 세금 및 보험 계산 메뉴 함수
def tax_and_insurance_menu():
    print("세금 및 보험 계산 항목을 선택하세요: ")
    print("1: 근로소득세 계산")
    print("2: 부가가치세 계산")
    print("3: 4대 보험 계산")
    choice = input("선택: ")

    if choice == "1":
        calculate_income_tax()
    elif choice == "2":
        calculate_vat()
    elif choice == "3":
        calculate_insurance()
    else:
        print("잘못된 선택입니다.")

# 프로그램 종료 여부를 판단하는 변수
b_is_exit = 0

# 메인 루프
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
    elif func == "6":
        tax_and_insurance_menu()  # 세금 및 보험 계산 메뉴 호출
    elif func == "7":
        user_id = input("사용자 ID를 입력하세요: ")
        user_info = open_account_info(user_id)
        if user_info:
            print(f"사용자 ID: {user_info['user_id']}")
            print(f"잔고: {user_info['bal']}")
            if user_info['history']:
                print("지출/수입 내역:")
                for date, transactions in user_info['history'].items():
                    print(f"날짜: {date}")
                    for amount, description in transactions:
                        print(f"    금액: {amount}, 내용: {description}")
            else:
                print("지출/수입 내역이 없습니다.")
    elif func == "8":
        add_memo()
    elif func == "?":
        print_help()
    elif func == "exit":
        b_is_exit = True
    else:
        print("올바른 기능을 입력해 주세요.")

