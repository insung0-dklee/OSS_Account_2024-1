import hashlib #hashlib 사용
import os
import json
from datetime import datetime
import pickle


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
    6: 지출 내역 수정
    7: 지출 내역 삭제
    8: 메모
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
            # 지출 내역의 금액을 숫자로 변환하여 더함
            monthly_total += float(entry["amount"])
            
            print(entry)
    print(f"{month}월 총 지출: {monthly_total} 원")

# 예산 설정 및 초과 알림 함수
def set_budget():
    budget = float(input("예산 설정 (원): "))
    # 저장된 지출 내역의 금액을 숫자로 변환하여 더함
    current_total = sum(float(entry["amount"]) for entry in ledger)
   
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
        category_totals[category] += float(entry["amount"])
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

# 지출 내역 삭제 함수
def delete_expense():
    # 저장된 지출 내역이 없는 경우
    if not ledger:
        print("저장된 지출 내역이 없습니다.")
        return
    
    # 저장된 지출 내역을 출력하여 사용자가 선택할 수 있도록 함
    print("저장된 지출 내역:")
    for idx, expense in enumerate(ledger, start=1):
        print(f"{idx}. 날짜: {expense['date']}, 카테고리: {expense['category']}, 설명: {expense['description']}, 금액: {expense['amount']}원")
    
    # 사용자로부터 삭제할 지출 항목의 번호를 입력받음
    index = input("삭제할 지출 항목의 번호를 입력하세요: ")

    try:
        index = int(index)
        # 입력받은 인덱스가 유효한지 확인하고 삭제
        if 1 <= index <= len(ledger):
            deleted_expense = ledger.pop(index - 1)
            print(f"다음 내역이 삭제되었습니다: {deleted_expense}")
        else:
            print("잘못된 번호입니다. 다시 시도하세요.")
    except ValueError:
        print("숫자를 입력하세요.")




from datetime import datetime

# 날짜 형식 검사 함수
# 날짜가 달력상 날짜인지 확인
def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        print("올바른 날짜 형식이 아닙니다. YYYY-MM-DD 형식으로 입력하세요.")
        return False
    
# 금액 형식 검사 함수 (소수점 포함)
def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        print("금액은 숫자 또는 소수점으로 입력하세요.")
        return False


# 지출 내역을 수정하는 함수
def modify_expense():
    # 저장된 지출 내역이 없는 경우
    if not ledger:
        print("저장된 지출 내역이 없습니다.")
        return
    
    # 저장된 지출 내역을 출력하여 사용자가 선택할 수 있도록 함
    print("저장된 지출 내역:")
    for idx, expense in enumerate(ledger, start=1):
        print(f"{idx}. 날짜: {expense['date']}, 카테고리: {expense['category']}, 설명: {expense['description']}, 금액: {expense['amount']}원")
    
    # 사용자로부터 수정할 지출 항목의 번호를 입력받음
    index = input("수정할 지출 항목의 번호를 입력하세요: ")
    
    try:
        index = int(index)
        #사용자에게 입력 받은 수정할 지출 항목의 내역을 출력한다
        if 1 <= index <= len(ledger):
            expense = ledger[index - 1]
            print(f"수정하고자 하는 지출 내역: {expense}")
            
            while True:
                # 새로운 값들을 입력 받음
                date = input(f"새 지출 날짜 (현재값: {expense['date']}) : ")
                # 입력 받은 값이  날짜 형식인지 검사
                if date and not validate_date(date):
                    continue  # 다시 입력 받기 위해 반복문의 처음으로 이동
                category = input(f"새 카테고리 (현재값: {expense['category']}) : ")
                description = input(f"새 설명 (현재값: {expense['description']}) : ")
                
                amount = input(f"새 금액 (현재값: {expense['amount']}) : ")
                
                # 입력 받은 금액 값이  숫자 형식 인지 검사
                if amount and not validate_amount(amount):
                    continue  # 다시 입력 받기 위해 반복문의 처음으로 이동
                
                # 데이터 형식에 맞게 입력 받았다면 입력 받은 값으로 업데이트
                expense['date'] = date if date else expense['date']
                expense['category'] = category if category else expense['category']
                expense['description'] = description if description else expense['description']
                expense['amount'] = amount if amount else expense['amount']
                
                # 입력 받은 값이 모두 유효한 경우 반복문 종료
                break
            
            print("지출 내역이 수정되었습니다.")
        else:
            print("잘못된 번호입니다. 다시 시도하세요.")
    except ValueError:
        print("숫자를 입력하세요.")




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
        modify_expense()
    elif func == "7":
        delete_expense()
    elif func =="8":
        add_memo()
    elif func == "?":
        print_help()
    elif func == "exit":
        b_is_exit = True
    elif func == "메모장":
        add_memo()
    else:
        b_is_exit = not b_is_exit

        print("올바른 기능을 입력해 주세요.")