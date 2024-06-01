import hashlib #hashlib 사용
import os
import json
from datetime import datetime
import pickle
import Account_book

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

def user_reg() : #회원가입
    id = input("id 입력: " ) #회원가입 시의 id 입력

    pw = input("password 입력: ") #회원가입 시의 pw 입력

    h = hashlib.sha256() #hashlib 모듈의 sha256 사용
    h.update(pw.encode()) #sha256으로 암호화
    pw_data = h.hexdigest() #16진수로 변환

    f = open('login.txt', 'wb') #login 파일 오픈

    userdata[id] = pw_data #key에 id값을, value에 비밀번호 값

    with open('login.txt', 'a', encoding='UTF-8') as fw: #utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items(): #딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n') #key, value값을 차례로 login.txt파일에 저장

def day_spending(hist, spending, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    """
    일자와 시간을 지정하여 해당 일자의 지출을 dictionary에 리스트 및 튜플 형태로 기록.
    parameters -
    hist : 기록하고자 하는 dictionary
    spending : 지출 액수
    where : 지출 장소, 혹은 지출 이유 등등. 미기재 가능.
    year, month, day, hour : 지정된 일자의 년, 월, 일. 미기재 가능 (미기재 시 현재의 년월일시로 자동 지정됨)
    """

    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:     # 해당 일자에 수입지출 내역이 없을 시,
        hist[f"{dt}"] = []      # 새 리스트 생성
    hist[f"{dt}"].append((-spending, where))

def day_income(hist, income, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    """
    일자와 시간을 지정하여 해당 일자의 수입을 dictionary에 리스트 및 튜플 형태로 기록.
    parameters -
    hist : 기록하고자 하는 dictionary
    income : 수입 액수
    where : 지출 장소, 혹은 지출 이유 등등. 미기재 가능.
    year, month, day, hour : 지정된 일자의 년, 월, 일. 미기재 가능 (미기재 시 현재의 년월일시로 자동 지정됨)
    """

    dt = datetime(year, month, day, hour)
    if f"{dt}" not in hist:     # 해당 일자에 수입지출 내역이 없을 시,
        hist[f"{dt}"] = []      # 새 리스트 생성
    hist[f"{dt}"].append((income, where))

def new_account(user_id, bal):
    """
    새 계정이 이용될 때, user_id와 bal, history를 포함한 dictionary를 생성하여 저장
    parameters -
    user_id : 사용자 이름
    bal : 잔고
    """
    household_ledger = {'user_id':user_id, 'bal':bal, 'history':{}}

    with open(f'{user_id}.txt', 'wb') as info:
        # pickle의 dump 기능을 이용하여 이용자의 이름으로 된 파일에
        # 이용자의 id, 잔고, 수입/지출 내역(해당 함수 내에서는 초기값 공백)을 저장
        pickle.dump(household_ledger,info)

def open_account_info(user_id):
    """
    user_id의 id를 사용하는 유저의 정보가 저장된 파일을 열어
    해당 유저의 id, 잔고, 지출/수입 내역이 담긴 dictionary를 return.
    """
    try:
        with open(f'{user_id}.txt', 'rb') as info:
            user_dict = pickle.load(info)
        return user_dict
    except Exception as e:
        print(f"{user_id}의 정보를 불러오는 과정에서 오류가 발생하였습니다. : {e}")
        return None

def calculator():
    try:
        # 사용자가 계산할 수식을 입력받는다.
        expr = input("계산할 수식을 입력하세요 (예: 2 + 3 * 4): ")

        # eval() 함수를 사용하여 입력된 수식을 평가하고 결과를 result에 저장한다.
        # eval() 함수는 입력된 문자열을 파이썬 표현식으로 계산해준다.
        result = eval(expr)

        # 계산 결과를 출력한다.
        print(f"결과: {result}")
    except Exception as e:
        # 계산 중 오류가 발생하면 예외를 처리하고 오류 메시지를 출력한다.
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

"""
add_memo : 파일 입출력을 사용하여 메모장을 추가할 수 있는 기능으로 예상지출내역, 오늘의 목표등을 기록할 수 있다.
@Parm
    None
@Return
    None
"""
def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title,"w",encoding="utf8")
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
    # 파일을 열어 기존 데이터를 불러옴
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    # 새 지출 내역을 리스트에 추가
    data.append(expense)
    # 데이터를 파일에 저장
    with open(expenses_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 저장된 지출 내역을 조회하는 함수
def view_expenses():
    # 파일을 열어 데이터를 불러옴
    with open(expenses_file, 'r') as file:
        data = json.load(file)
        if data:
            # 데이터가 존재하면 각 지출 내역을 출력
            for idx, expense in enumerate(data, start=1):
                print(f"{idx}. {expense['date']} - {expense['item']} : {expense['amount']}원")
        else:
            # 데이터가 비어 있으면 해당 메시지 출력
            print("저장된 지출 내역이 없습니다.")

# 지출 내역을 입력받는 함수
def input_expense():
    # 사용자로부터 지출 날짜, 항목, 금액을 입력받음
    date = input("지출 날짜 (예: 2024-05-30): ")
    item = input("지출 항목: ")
    amount = input("지출 금액: ")
    # 입력받은 데이터를 딕셔너리 형태로 저장
    expense = {
        'date': date,
        'item': item,
        'amount': amount
    }
    # 지출 내역을 파일에 저장
    save_expense(expense)
    print("지출 내역이 저장되었습니다.")

# 기능 3: 지출 내역 삭제
def delete_expense():
    # 삭제할 지출 항목의 인덱스를 입력받음
    index = input("삭제할 지출 항목의 번호를 입력하세요: ")

    # 저장된 지출 내역을 불러옴
    with open(expenses_file, 'r') as file:
        data = json.load(file)
    # 입력받은 인덱스가 유효한지 확인하고 삭제
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

#가계부 초깃값 임의로 설정
a = Account_book("가계부 1",1000000)
b = Account_book("가계부 2",2000000)
c = Account_book("가계부 3",3000000)

Account_list = [a,b,c] #가계부 리스트
i=0

def choose_Account(func):#가계부 선택 함수
    print("가계부 선택(번호로 입력)")
    for i in range(0,len(Account_list)):#가계부 리스트 출력
      print(f"가계부 {i+1}번 : ",Account_list[i].name)
    choose = input()
    return choose 

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
    elif func == "?":
        print_help()
    elif func == "exit":
        b_is_exit = True
    elif func == "메모장":
        add_memo()
    else:
        b_is_exit = not b_is_exit

        print("올바른 기능을 입력해 주세요.")

#내 계좌에 이체한 금액을 지출로 인식하지 않게 하는 기능 추가


class BankAccount:
    def __init__(self, owner_name, balance=0): #예금주명, 잔액 초기화
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount): #지정 금액을 입금
        self.balance += amount

    def withdraw(self, amount): #현재 계좌 잔액이 지정 금액보다 많거나 같으면 현재 계좌에서 지정 금액 만큼 출금
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("잔액이 부족합니다.") #잔액이 부족할 경우 잔액 부족 메시지 출력
            return False

    def transfer(self, other_account, amount): #현재 계좌에서 다른 계좌로 지정 금액을 이체
        if self.owner_name == other_account.owner_name:
            if self.withdraw(amount): #예금주명이 같은 계좌간의 이체인 경우
                other_account.deposit(amount)
                print("내 통장으로 옮기기 성공")
            else:
                print("내 통장으로 옮기기 실패")
        else:
            if self.withdraw(amount): #예금주명이 다른 계좌간의 이체인 경우
                other_account.deposit(amount)
                print("이체 성공")
            else:
                print("이체 실패")


#계좌 잔액 확인
class AccountBalance: #계좌 잔액을 확인하는 AccountBalance 클래스 생성
    def __init__(self): 
        self.accounts = {} #계좌의 정보를 저장할 딕셔너리 초기화

    def register_account(self, name, balance): #계좌의 이름과 잔액을 입력받아 딕셔너리에 저장
        if name in self.accounts:
            print(f"오류: '{name}' 계좌가 이미 등록되어 있습니다.")
        else:
            self.accounts[name] = balance
            print(f"'{name}' 계좌가 {balance} 원으로 등록되었습니다.")

    def check_balance(self, name): #계좌의 이름을 입력받아 잔액을 출력, 등록되지 않은 이름 입력 시 오류 메시지 출력
        if name in self.accounts:
            print(f"'{name}' 계좌의 잔액은 {self.accounts[name]} 원입니다.")
        else:
            print(f"오류: '{name}' 계좌가 존재하지 않습니다.")

def main():
    account_balance = AccountBalance()
    #사용자로부터 초기 계좌 등록을 위한 정보를 입력 받음
    print("***초기 계좌 등록***")
    while True:
        name = input("계좌 이름을 입력하세요 (종료하려면 '종료' 입력): ")
        if name.lower() == '종료':
            break
        balance_str = input(f"{name} 계좌 잔액을 입력하세요: ")
        try:
            balance = float(balance_str)
            account_balance.register_account(name, balance)
        except ValueError:
            print("오류: 잔액은 숫자로 입력되어야 합니다.")
            
    #계좌 등록이 끝났다면 사용자가 잔액을 확인하고 싶은 계좌 이름을 입력받아 잔액을 확인할 수 있음
    while True:
        print("\n--- 계좌 관리 ---")
        print("1. 계좌 등록")
        print("2. 잔액 확인")
        print("3. 종료")

        choice = input("옵션을 선택하세요 (1-3): ")

        if choice == '1':
            name = input("계좌 이름을 입력하세요: ")
            if name in account_balance.accounts:
                print(f"오류: '{name}' 계좌가 이미 등록되어 있습니다.")
            else:
                balance_str = input("계좌 잔액을 입력하세요: ")
                try:
                    balance = float(balance_str)
                    account_balance.register_account(name, balance)
                except ValueError:
                    print("오류: 잔액은 숫자로 입력되어야 합니다.")

        elif choice == '2':
            name = input("잔액을 확인할 계좌 이름을 입력하세요: ")
            account_balance.check_balance(name)

        elif choice == '3':
            print("계좌 관리를 종료합니다.")
            break

        else:
            print("잘못된 옵션입니다. 올바른 옵션을 선택하세요.")

if __name__ == "__main__":
    main()



#가계부 다이어리 작성 및 조회 기능
import datetime

class Diary:
    def __init__(self):
        self.entries = {} #다이어리 항목을 저장
        self.monthly_spending_goals = {} #월별 지출 목표를 저장

    def validate_date(self, date_str): #입력한 날짜 문자열이 올바른 형식인지 확인
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def add_entry(self): #다이어리 내용 작성
        date_str = input("날짜를 입력하세요 (YYYY-MM-DD): ")
        if not self.validate_date(date_str):
            print("날짜 입력 형식에 맞지 않습니다. 다시 입력해주세요.")
            return

        while True:
            expenditure_input = input("지출을 입력하세요: ")
            if expenditure_input.replace('.', '', 1).isdigit():
                expenditure = float(expenditure_input)
                break
            else:
                print("숫자만 입력 가능합니다.")

        while True:
            income_input = input("수입을 입력하세요: ")
            if income_input.replace('.', '', 1).isdigit():
                income = float(income_input)
                break
            else:
                print("숫자만 입력 가능합니다.")

        self.entries[date_str] = {
            'expenditure': expenditure,
            'income': income
        }

        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj.day == 1:
            last_month_total_expenditure = self.calculate_last_month_expenditure(date_obj)
            print(f"저번 달 총 지출 금액: {last_month_total_expenditure}")

            while True:
                try:
                    spending_goal = float(input("이번 달 목표 지출 금액을 입력하세요: "))
                    break
                except ValueError:
                    print("숫자만 입력 가능합니다.")

            self.monthly_spending_goals[date_obj.strftime('%Y-%m')] = spending_goal

        print("다이어리 작성이 완료되었습니다.")

    def calculate_last_month_expenditure(self, date_obj): #입력한 날짜 이전 달의 총 지출 금액을 계산
        last_month = (date_obj.replace(day=1) - datetime.timedelta(days=1)).strftime('%Y-%m')
        total_expenditure = 0.0
        for date_str, entry in self.entries.items():
            if date_str.startswith(last_month):
                total_expenditure += entry['expenditure']
        return total_expenditure

    def view_entry(self): #입력한 날짜에 작성했던 다이어리를 조회
        date_str = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
        if not self.validate_date(date_str):
            print("날짜 입력 형식에 맞지 않습니다. 다시 입력해주세요.")
            return

        entry = self.entries.get(date_str)
        if entry:
            print(f"날짜: {date_str}")
            print(f"지출: {entry['expenditure']}")
            print(f"수입: {entry['income']}")
            print("다이어리 조회가 완료되었습니다.")
        else:
            print("해당 날짜에 작성된 다이어리가 없습니다.")

def main():
    diary = Diary()
    while True:
        print("\n**** 가계부 다이어리 ****")
        print("1. 다이어리 작성하기")
        print("2. 다이어리 조회하기")
        print("3. 종료하기")
        choice = input("선택하세요: ")

        if choice == '1':
            diary.add_entry()
        elif choice == '2':
            diary.view_entry()
        elif choice == '3':
            print("가계부 다이어리 기능을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()