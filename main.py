import hashlib #hashlib 사용
<<<<<<< .merge_file_n78cyB
import os
import json
from datetime import datetime
import pickle
=======
import json
import os
>>>>>>> .merge_file_tby6Wu

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

<<<<<<< .merge_file_n78cyB
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
    6: 주식 수익 기록
    7: 주식 수익 조회
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

def record_stock_profit():
    # stock_profits.json 파일이 존재하지 않는 경우 빈 파일을 생성
    if not os.path.exists('stock_profits.json'):
        with open('stock_profits.json', 'w') as file:
            json.dump([], file)

    date = input("날짜 (YYYY-MM-DD): ")
    stock_name = input("주식 종목명: ")
    buy_price = float(input("매입 가격: "))
    sell_price = float(input("매도 가격: "))
    profit = sell_price - buy_price

    # 기록할 주식 수익 정보를 딕셔너리로 생성
    stock_profit = {
        "date": date,
        "stock_name": stock_name,
        "buy_price": buy_price,
        "sell_price": sell_price,
        "profit": profit
    }

    # 기존 파일의 데이터를 불러옴
    with open('stock_profits.json', 'r') as file:
        data = json.load(file)

    # 새로운 주식 수익 정보를 추가
    data.append(stock_profit)

    # 데이터를 파일에 다시 저장
    with open('stock_profits.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("주식 수익이 성공적으로 기록되었습니다.")

def view_stock_profit():
    """
    사용자가 입력한 날짜에 해당하는 주식 수익 정보를 조회하는 함수
    """
    date = input("조회할 날짜 (YYYY-MM-DD): ")

    # 파일이 존재하지 않는 경우, 빈 리스트를 반환
    if not os.path.exists('stock_profits.json'):
        print("주식 수익 기록이 없습니다.")
        return

    # 파일이 존재하는 경우, 주식 수익 정보를 불러옴
    with open('stock_profits.json', 'r') as file:
        data = json.load(file)

    found = False
    # 사용자가 입력한 날짜와 동일한 날짜의 주식 수익 정보를 출력
    for profit in data:
        if profit['date'] == date:
            print(f"날짜: {profit['date']}, 주식 종목명: {profit['stock_name']}, 매입 가격: {profit['buy_price']}, 매도 가격: {profit['sell_price']}, 수익: {profit['profit']}")
            found = True

    # 해당 날짜의 주식 수익 정보가 없는 경우 메시지 출력
    if not found:
        print("해당 날짜의 주식 수익 정보가 없습니다.")


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
        record_stock_profit()
    elif func == "7":
        view_stock_profit()
    elif func == "?":
        print_help()
    elif func == "exit":
        b_is_exit = True
    elif func == "메모장":
        add_memo()
    else:
        b_is_exit = not b_is_exit

        print("올바른 기능을 입력해 주세요.")
        
=======
class HouseholdAccountBook:
    def __init__(self, data_file='account_book_data.json'):
        self.data_file = data_file
        self.monthly_budget = {}
        self.records = []
        self.load_data()

    def set_monthly_budget(self, month, year, budget):
        self.monthly_budget[f'{year}-{month:02d}'] = budget
        self.save_data()

    def get_monthly_budget(self, month, year):
        return self.monthly_budget.get(f'{year}-{month:02d}', None)

    def budget_status(self, month, year):
        budget = self.get_monthly_budget(month, year)
        if budget is None:
            return "요청하신 달은 지출 목표가 없습니다."
        else:
            return f"요청하신 달의 지출 목표는 {budget}."

    def save_data(self):
        data = {
            'monthly_budget': self.monthly_budget,
            'records': self.records
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.monthly_budget = data.get('monthly_budget', {})
                self.records = data.get('records', [])

def print_help():
    print("""
    1: 월별 예산 설정
    2: 현재 예산 상태 확인
    3: 없음
    ?: 도움말
    exit: 프로그램 종료
    """)

def main():
    account_book = HouseholdAccountBook()
    b_is_exit = 0

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
            year = int(input("년 입력 (YYYY): "))
            month = int(input("월 입력 (MM): "))
            budget = int(input("예산 금액 입력: "))
            account_book.set_monthly_budget(month, year, budget)
            print("월별 예산이 설정되었습니다.")

        elif func == "2":
            year = int(input("년 입력 (YYYY): "))
            month = int(input("월 입력 (MM): "))
            status = account_book.budget_status(month, year)
            print(status)

        elif func == "3":

            break
        elif func == "?":
            print_help()

        elif func.lower() == "exit":
            b_is_exit = 1

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            print_help()

if __name__ == "__main__":
    main()
    
>>>>>>> .merge_file_tby6Wu
