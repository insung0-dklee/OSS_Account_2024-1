import hashlib #hashlib 사용
import os
import json
from datetime import datetime, date
import pickle
import Account_book
import random
import webbrowser
import re

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

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

class User:    # 사용자 정보 저장 (이름)
    def __init__(self, name):
        self.name = name

# 아이디, 비밀번호, 이름, 전화번호를 저장해둘 딕셔너리
userdata2 = {}
# 이름과 아이디를 매핑하기 위한 딕셔너리
usernames = {}
# 전화번호와 아이디를 매핑하기 위한 딕셔너리
userphones = {}

def user_reg_include_name_phone():  # 이름과 전화번호 정보를 포함한 회원가입
    id = input("id 입력: ")  # 회원가입 시의 id 입력
    name = input("이름 입력: ")  # 회원가입 시의 이름 입력
    phone = input("전화번호 입력: ")  # 회원가입 시의 전화번호 입력

    # 전화번호 중복 체크 - 중복된 전화번호는 가입 불가
    if phone in userphones:
        print("이미 등록된 전화번호입니다. 다른 전화번호를 사용해주세요.")
        return

    pw = input("password 입력: ")  # 회원가입 시의 pw 입력

    h = hashlib.sha256()  # hashlib 모듈의 sha256 사용
    h.update(pw.encode())  # sha256으로 암호화
    pw_data = h.hexdigest()  # 16진수로 변환

    userdata2[id] = {'pw': pw_data, 'name': name, 'phone': phone}  # key에 id값을, value에 비밀번호와 이름, 전화번호 값
    usernames[name] = id  # 이름과 아이디 매핑
    userphones[phone] = id  # 전화번호와 아이디 매핑

    with open('login.txt', 'w', encoding='UTF-8') as fw:  # utf-8 변환 후 login.txt에 작성
        for user_id, user_info in userdata2.items():  # 딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_info["pw"]} : {user_info["name"]} : {user_info["phone"]}\n')  # 아이디, 비밀번호, 이름, 전화번호 값을 차례로 login.txt파일에 저장


"""
전화번호를 통해 아이디를 찾는 함수
"""
def find_id_by_phone():
    phone = input("찾고자 하는 사용자의 전화번호 입력: ")  # 사용자가 찾고자 하는 전화번호를 입력받음
    if phone in userphones:  # 입력받은 전화번호가 userphones 딕셔너리에 존재하는지 확인
        print(f'해당 전화번호로 등록된 아이디는 {userphones[phone]}입니다.')  # 존재하면 해당 전화번호에 매핑된 아이디를 출력
    else:
        print("해당 전화번호를 가진 사용자가 없습니다.")  # 존재하지 않으면 사용자 없음 메시지 출력

"""
회원 정보를 수정하는 함수
"""
def modify_user_info():
    id_to_modify = input("수정할 사용자의 id 입력: ")  # 수정하고자 하는 사용자의 id 입력

    # 해당 id가 userdata2에 존재하는지 확인
    if id_to_modify not in userdata2:
        print("해당 아이디를 가진 사용자가 없습니다.")
        return

    # 수정할 정보 입력
    new_name = input("새로운 이름 입력: ")  # 새로운 이름 입력
    new_phone = input("새로운 전화번호 입력: ")  # 새로운 전화번호 입력

    # 전화번호 중복 체크 - 중복된 전화번호는 수정 불가
    if new_phone in userphones and userphones[new_phone] != id_to_modify:
        print("이미 등록된 전화번호입니다. 다른 전화번호를 사용해주세요.")
        return

    new_pw = input("새로운 password 입력: ")  # 새로운 pw 입력

    h = hashlib.sha256()  # hashlib 모듈의 sha256 사용
    h.update(new_pw.encode())  # sha256으로 암호화
    new_pw_data = h.hexdigest()  # 16진수로 변환

    # 사용자 정보 수정
    userdata2[id_to_modify] = {'pw': new_pw_data, 'name': new_name, 'phone': new_phone}

    # 이름과 전화번호 매핑 정보 수정
    # 이전 이름과 전화번호 삭제
    old_phone = [key for key, value in userphones.items() if value == id_to_modify][0]
    del userphones[old_phone]
    # 새로운 이름과 전화번호 매핑
    usernames[new_name] = id_to_modify
    userphones[new_phone] = id_to_modify

    # 수정된 정보를 파일에 다시 쓰기
    with open('login.txt', 'w', encoding='UTF-8') as fw:
        for user_id, user_info in userdata2.items():
            fw.write(f'{user_id} : {user_info["pw"]} : {user_info["name"]} : {user_info["phone"]}\n')

    print("사용자 정보가 성공적으로 수정되었습니다.")

class JointAccount:    # 공동 계정 정보 관리 (계정 이름, 사용자 목록, 거래 내역, 잔액)
    def __init__(self, account_name):
        self.joint_account = account_name    # 공동 계정 이름
        self.joint_users = []    # 추가한 사용자 리스트
        self.joint_tran = []    # 거래 내역 리스트
        self.joint_bal = 0    # 현재 잔액

    def add_joint_user(self, joint_user):    # 계정에 사용자 추가
        self.joint_users.append(joint_user)

    def add_joint_income(self, amount, joint_desc=""):    # 수입 내역 추가 및 수입에 대한 설명
        self.joint_tran.append({"type": "income", "amount": amount, "income_description": joint_desc})
        self.joint_bal += amount

    def add_joint_expense(self, amount, joint_desc=""):    # 지출 내역 추가 및 지출에 대한 설명
        self.joint_tran.append({"type": "expense", "amount": amount, "expense_description": joint_desc})
        self.joint_bal -= amount

    def get_joint_bal(self):    # 현재 잔액 반환
        return self.joint_bal

    def get_joint_tran(self):    # 거래 내역 반환
        return self.joint_tran

def export_account(account):
    """
    가계부 데이터를 JSON 파일로 내보내기.
    parameters -
    account : 내보낼 가계부 객체
    """
    filename = f"{account.name}_export.json"
    account_data = {
        'name': account.name,
        'balance': account.balance,
        'history': account.history
    }
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(account_data, file, ensure_ascii=False, indent=4)
    print(f"{filename} 파일로 가계부 데이터가 저장되었습니다.")

def import_account():
    """
    JSON 파일로부터 가계부 데이터를 가져와 가계부 리스트에 추가하기.
    """
    filename = input("가져올 가계부 파일명을 입력하세요 (예: my_account_export.json): ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            account_data = json.load(file)
        new_account = Account_book(account_data['name'], account_data['balance'])
        new_account.history = account_data['history']
        Account_list.append(new_account)
        print(f"{account_data['name']} 가계부가 성공적으로 추가되었습니다.")
    except Exception as e:
        print(f"파일을 가져오는 중 오류가 발생했습니다: {e}")

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

def read_memo():
    print("열고 싶은 메모장 제목: ")
    str_title = input()
    try:
        with open(str_title, "r", encoding="utf8") as f:
            content = f.read()
            print("메모 내용:")
            print(content)
    except FileNotFoundError:
        print("해당 제목의 메모장을 찾을 수 없습니다.")

def delete_memo():
    print("삭제할 메모장 제목: ")
    str_title = input()
    if os.path.exists(str_title):
        os.remove(str_title)
        print(f"{str_title} 메모가 삭제되었습니다.")
    else:
        print("해당 제목의 메모장을 찾을 수 없습니다.")

def memo():
    print("1. 메모 추가")
    print("2. 메모 읽기")
    print("3. 메모 삭제")
    choice = input("선택: ")
    if choice == "1":
        add_memo()
    elif choice == "2":
        read_memo()
    elif choice == "3":
        delete_memo()
    else:
        print("잘못된 선택입니다.")



def guide_link():
    webbrowser.open("https://help.3o3.co.kr/hc/ko/articles/15516331018521")

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
        user_id_clean = re.sub(r'[^a-zA-Z)-9]', '-', user_id)
        with open(f'{user_id_clean}.txt', 'rb') as info:
            user_dict = pickle.load(info)
        return user_dict
    except Exception as e:
        print(f"{user_id_clean}의 정보를 불러오는 과정에서 오류가 발생하였습니다. : {e}")
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

"""
가계부 데이터 및 사용자 데이터를 초기화하는 함수.
가계부 데이터와 사용자 데이터를 빈 상태로 설정하고, 지출 내역 파일을 초기화한다.
"""
def reset_data():
    global ledger, userdata
    # 가계부 데이터와 사용자 데이터를 초기화
    ledger = []
    userdata = {}
    # 지출 내역 파일을 초기화
    with open(expenses_file, 'w') as file:
        json.dump([], file)
    # 로그인 파일이 존재하는 경우 삭제
    if os.path.exists('login.txt'):
        os.remove('login.txt')
    print("모든 데이터가 초기화되었습니다.")

def get_valid_amount_input(): 
    """
    사용자로부터 유효한 금액을 입력받는 함수.
    입력이 올바르지 않을 경우, 사용자로부터 반복하여 입력을 받음.
    """
    while True:
        amount = input("금액: ") # 사용자로부터 금액 입력 요청
        if amount.isdigit(): # 입력이 숫자로만 이루어져 있는지 확인
            return float(amount) # 숫자로만 이루어져 있다면 입력값을 float로 변환하여 반환
        else:
            print("숫자만 입력하세요.") # 입력이 숫자가 아닌 경우, 오류 메시지 출력

# 수입/지출 항목 추가 함수
def add_entry():
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    score = day_evaluation()
    amount = get_valid_amount_input()  # 수정된 부분! 금액 입력 요청 및 유효성 검사.
    entry = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
        "score": score  # 평가 점수 추가
    }
    ledger.append(entry)
    print("항목이 추가되었습니다.")

# 항목 조회 함수
def view_entries():
    for entry in ledger:
        print(entry)
        if "score" in entry:
            print(f"평가 점수: {entry['score']}")


def day_evaluation():
    # 사용자로부터 그날의 평가를 입력 받음
    evaluation = input("오늘의 평가를 입력하세요 (0에서 10까지): ")
    try:
        evaluation = float(evaluation)
        if 0 <= evaluation <= 10:
            print(f"오늘의 평가는 {evaluation}점입니다.")
            return evaluation
        else:
            print("평가는 0에서 10 사이의 숫자여야 합니다.")
            return None
    except ValueError:
        print("올바른 숫자를 입력하세요.")
        return None

def calculate_average_score(scores):
    if scores:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        return average_score
    else:
        return None

def compare_financial_goal(user1, user2, goal):
    """
    두 사용자의 잔고를 비교하여 목표 금액에 대한 달성률을 계산하고 비교합니다.
    
    @Param
        user1 : User object : 비교할 첫 번째 사용자 객체.
        user2 : User object : 비교할 두 번째 사용자 객체.
        goal : float : 달성하고자 하는 목표 금액.
    @Return
        None
    @Raises
        목표 금액이 음수이거나 0일 경우, 오류 메시지를 출력하고 함수를 종료합니다.
    """
    if goal <= 0:
        print("목표 금액은 양수여야 합니다.")
        return

    user1_progress = (user1.balance / goal) * 100
    user2_progress = (user2.balance / goal) * 100

    print(f"{user1.name}의 목표 달성률: {user1_progress:.2f}%")
    print(f"{user2.name}의 목표 달성률: {user2_progress:.2f}%")

    if user1_progress > user2_progress:
        print(f"{user1.name}의 목표 달성률이 더 높습니다.")
    elif user1_progress < user2_progress:
        print(f"{user2.name}의 목표 달성률이 더 높습니다.")
    else:
        print("두 사용자의 목표 달성률이 같습니다.")

# 월별 보고서 생성 함수
def generate_monthly_report():
    month = input("보고서 생성할 월 (YYYY-MM): ")
    monthly_total = 0
    scores = []  # 평가 점수를 저장할 리스트
    category_totals = {}
    for entry in ledger:
        if entry["date"].startswith(month):
            monthly_total += float(entry["amount"])
            category = entry["category"]
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += entry["amount"]
            print(entry)
            if "score" in entry:
                scores.append(entry["score"])  # 평가 점수를 리스트에 추가
    print(f"{month}월 총 지출: {monthly_total} 원")
    print(f"{month}월 각 카테고리별 지출 내역:")
    for category, total in category_totals.items():
        print(f"{category}: {total} 원")

    average_score = calculate_average_score(scores)
    if category_totals:
        max_category = max(category_totals, key=category_totals.get)
        print(f"\n가장 지출이 많은 카테고리: {max_category} ({category_totals[max_category]} 원)")
    else:
        print("해당 월에는 지출 내역이 없습니다.")
    
    if average_score is not None:
        print(f"{month}월 평균 점수: {average_score:.2f} 점")
    else:
        print(f"{month}월에는 평가된 점수가 없습니다.")

budget = None #전역변수 budget의 기본값 설정

# 예산 설정 및 초과 알림 함수
def set_budget():
    global budget 
    budget = float(input("예산 설정 (원): ")) #budget을 전역변수로 변경
    current_total = sum(float(entry["amount"]) for entry in ledger)
    if current_total > budget:
        print(f"경고: 예산 초과! 현재 지출: {current_total} 원")
    else:
        print(f"예산 설정 완료. 현재 지출: {current_total} 원, 남은 예산: {budget - current_total} 원")

# 예산 확인 함수
def check_budget():
    global budget
    if budget is None:
        print("예산이 지정되지 않았습니다.")
    else:
        current_total = sum(entry["amount"] for entry in ledger)
        print(f"설정된 예산은 {budget}원이고, 남은 예산은 {budget - current_total} 원입니다.")

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

def calculate_monthly_savings(target_amount, target_date):
    """
    목표 금액과 목표 날짜를 기준으로 매월 저축해야 할 금액과 남은 달 수를 계산합니다.
    
    @Param
        target_amount : 목표 금액.
        target_date : 목표 날짜 (YYYY-MM-DD 형식).
    @Return
        monthly_savings : 매월 저축해야 할 금액.
        months_left : 남은 달 수.
    @Raises
        날짜 관련 연산에서 예외가 발생할 경우 에러 메시지를 출력합니다.
    """
    today = date.today()
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()

    months_left = (target_date.year - today.year) * 12 + target_date.month - today.month

    monthly_savings = target_amount / months_left

    print(f"매월 저축해야 할 금액: {monthly_savings:.2f}원, 남은 달 수: {months_left}개월")
    return monthly_savings, months_left


def track_savings(savings, target_amount, months_left):
    """
    현재까지의 저축액, 목표 금액, 매월 저축해야 할 금액, 남은 달 수를 바탕으로 남은 금액과 수정된 월간 저축액을 계산합니다.
    
    @Param
        savings : 현재까지 저축된 금액.
        target_amount : 목표 금액.
        monthly_savings : 매월 저축해야 할 금액.
        months_left : 남은 달 수.
    @Return
        remaining_amount : 남은 금액.
        updated_monthly_savings : 수정된 월간 저축액.
    @Raises
        날짜 관련 연산에서 예외가 발생할 경우 에러 메시지를 출력합니다.
    """

    remaining_amount = target_amount - savings
    updated_monthly_savings = remaining_amount / months_left

    print(f"남은 금액: {remaining_amount:.2f}원, 수정된 월간 저축액: {updated_monthly_savings:.2f}원")
    return remaining_amount, updated_monthly_savings

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

monthly_goals = {}

def set_monthly_goal(month, amount):
    """월별 목표 금액을 설정합니다."""
    monthly_goals[month] = amount
    print(f"{month}의 목표 금액이 {amount}원으로 설정되었습니다.")

def get_monthly_goal(month):
    """월별 목표 금액을 반환합니다."""
    return monthly_goals.get(month, "해당 월에 대한 목표 금액이 설정되지 않았습니다.")

def show_all_goals():
    """모든 월별 목표 금액을 출력합니다."""
    if not monthly_goals:
        print("설정된 목표 금액이 없습니다.")
    else:
        for month, amount in monthly_goals.items():
            print(f"{month}: {amount}원")

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

#가계부 초깃값 임의로 설정
#Account_book.py의 Account book 모듈을 불러오므로 Account.
a = Account_book.Account_book("가계부 1",1000000)
b = Account_book.Account_book("가계부 2",2000000)
c = Account_book.Account_book("가계부 3",3000000)

Account_list = [a,b,c] #가계부 리스트
i=0

def choose_Account(func):#가계부 선택 함수
    print("가계부 선택(번호로 입력)")
    for i in range(0,len(Account_list)):#가계부 리스트 출력
      print(f"가계부 {i+1}번 : ",Account_list[i].name)
    choose = input()
    return choose 

"""
YU_Account : 프로그램 시작 화면 출력
@Parm
    None
@return
    None
"""
def YU_Account():
    welcome_message = """=======================================
*                                     *
*           YU_Account_Book           *
*                                     *
=======================================
-이 프로그램은 사용자가 재정을 효과적 
으로 관리할 수 있도록 도와줍니다.
    """
    print(welcome_message)

YU_Account() #프로그램 시작 화면

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
        memo()
    else:
        b_is_exit = not b_is_exit 

        print("올바른 기능을 입력해 주세요.")


# 카테고리 할당 기능추가
class AccountBook:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount, category=None):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount, category))

    def categorize_expense(self, amount, description):
        # 지출 내용을 분석하여 카테고리 할당
        keywords = {
            "food": ["식비", "음식", "식료품", "식사"],
            "transportation": ["교통", "버스", "지하철", "택시"],
            "entertainment": ["문화", "영화", "공연", "놀이"],
            "shopping": ["쇼핑", "상점", "마트", "구매"],
            "utilities": ["요금", "공과금", "전기", "수도"]
        }
        
        # 카테고리 할당
        category = "uncategorized"
        for key, values in keywords.items():
            for value in values:
                if value in description:
                    category = key
                    break
        return category

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def show_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)

# 가계부 인스턴스 생성
account_book = AccountBook()

# 지출 기록
account_book.deposit(2000)
account_book.withdraw(300, category=account_book.categorize_expense(300, "편의점에서 음료 구매"))
account_book.withdraw(500, category=account_book.categorize_expense(500, "영화 관람"))

# 잔액 및 거래 내역 출력
account_book.show_balance()
account_book.show_transactions()

# 지출예산 설정 및 알림 기능
class AccountBook:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.budgets = {}
        self.spending = {}

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount, description=""):
        category = self.categorize_expense(description)
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}원")
        else:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount, category, description))
            self.spending[category] = self.spending.get(category, 0) + amount
            self.check_budget(category)

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"Budget for {category} set to {amount}원")

    def check_budget(self, category):
        if category in self.budgets and self.spending.get(category, 0) > self.budgets[category]:
            print(f"Alert: You have exceeded the budget for {category}! (Budget: {self.budgets[category]}원, Spending: {self.spending[category]}원)")

    def categorize_expense(self, description):
        keywords = {
            "food": ["식비", "음식", "식료품", "식사"],
            "transportation": ["교통", "버스", "지하철", "택시"],
            "entertainment": ["문화", "영화", "공연", "놀이"],
            "shopping": ["쇼핑", "상점", "마트", "구매"],
            "utilities": ["요금", "공과금", "전기", "수도"]
        }
        category = "uncategorized"
        for key, values in keywords.items():
            for value in values:
                if value in description:
                    category = key
                    break
            if category != "uncategorized":
                break
        return category

    def show_balance(self):
        print(f"Current balance: {self.balance}원")

    def show_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            if transaction[0] == "Deposit":
                print(f"{transaction[0]}: +{transaction[1]}원")
            else:
                print(f"{transaction[0]}: -{transaction[1]}원, Category: {transaction[2]}, Description: {transaction[3]}")

    def show_budgets(self):
        print("Budgets:")
        for category, amount in self.budgets.items():
            print(f"{category}: {amount}원")

    def show_spending(self):
        print("Spending:")
        for category, amount in self.spending.items():
            print(f"{category}: {amount}원")

# 가계부 인스턴스 생성
account_book = AccountBook()

# 입출금 기록 및 예산 설정
account_book.deposit(5000)
account_book.set_budget("food", 1000)
account_book.set_budget("entertainment", 500)

account_book.withdraw(300, "편의점에서 음료 구매")
account_book.withdraw(800, "식사 비용")
account_book.withdraw(600, "영화 관람")

# 잔액, 거래 내역, 예산 및 지출 내역 출력
account_book.show_balance()
account_book.show_transactions()
account_book.show_budgets()
account_book.show_spending()


# 지출비교 및 지출경고 메시지 기능
import datetime

class AccountBook:
    def __init__(self, name, bal):
        self.name = name
        self.balance = bal if bal > 0 else 0
        self.income_total = self.balance
        self.income_list = [self.balance] if self.balance > 0 else []
        self.spend_total = 0
        self.spend_list = []
        self.transactions = [("Initial Balance", self.balance, "initial", "")]
        self.budgets = {}
        self.spending = {}
        self.monthly_spending = {}

        if bal <= 0:
            print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

    def get_current_month(self):
        now = datetime.datetime.now()
        return now.year, now.month

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount, "income", ""))
        self.income_total += amount
        self.income_list.append(amount)

    def withdraw(self, amount, description=""):
        category = self.categorize_expense(description)
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}원")
        else:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount, category, description))
            self.spend_total += amount
            self.spend_list.append(amount)
            self.spending[category] = self.spending.get(category, 0) + amount

            # Update monthly spending
            current_month = self.get_current_month()
            if current_month not in self.monthly_spending:
                self.monthly_spending[current_month] = 0
            self.monthly_spending[current_month] += amount

            self.check_budget(category)
            self.check_spending_increase()

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"Budget for {category} set to {amount}원")

    def check_budget(self, category):
        if category in self.budgets and self.spending.get(category, 0) > self.budgets[category]:
            print(f"Alert: You have exceeded the budget for {category}! (Budget: {self.budgets[category]}원, Spending: {self.spending[category]}원)")

    def categorize_expense(self, description):
        keywords = {
            "food": ["식비", "음식", "식료품", "식사"],
            "transportation": ["교통", "버스", "지하철", "택시"],
            "entertainment": ["문화", "영화", "공연", "놀이"],
            "shopping": ["쇼핑", "상점", "마트", "구매"],
            "utilities": ["요금", "공과금", "전기", "수도"]
        }
        category = "uncategorized"
        for key, values in keywords.items():
            for value in values:
                if value in description:
                    category = key
                    break
            if category != "uncategorized":
                break
        return category

    def check_spending_increase(self):
        current_month = self.get_current_month()
        previous_month = (current_month[0], current_month[1] - 1) if current_month[1] > 1 else (current_month[0] - 1, 12)

        if previous_month in self.monthly_spending:
            previous_spending = self.monthly_spending[previous_month]
            current_spending = self.monthly_spending.get(current_month, 0)
            if current_spending > previous_spending * 1.2:  # 20% increase threshold
                print(f"Warning: Your spending has increased significantly this month! (Previous: {previous_spending}원, Current: {current_spending}원)")

    def show_balance(self):
        print(f"Current balance: {self.balance}원")

    def show_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            if transaction[0] == "Deposit" or transaction[0] == "Initial Balance":
                print(f"{transaction[0]}: +{transaction[1]}원")
            else:
                print(f"{transaction[0]}: -{transaction[1]}원, Category: {transaction[2]}, Description: {transaction[3]}")

    def show_budgets(self):
        print("Budgets:")
        for category, amount in self.budgets.items():
            print(f"{category}: {amount}원")

    def show_spending(self):
        print("Spending:")
        for category, amount in self.spending.items():
            print(f"{category}: {amount}원")

    def income(self):
        try:
            income_money = int(input("수입을 입력하세요 "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return
        if income_money < 0:
            print("0 미만의 값을 입력하셨습니다.")
            return
        self.deposit(income_money)

    def spend(self):
        try:
            spend_money = int(input("지출을 입력하세요 "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return
        description = input("지출 설명을 입력하세요: ")
        if spend_money < 0 or spend_money > self.balance:
            print("값을 잘못 입력하셨습니다.")
            return
        self.withdraw(spend_money, description)

    def show_total(self):
        print("현재까지 소득의 총합은 ", self.income_total, "원 입니다.")
        print("현재까지 지출의 총합은 ", self.spend_total, "원 입니다.")

    def show_sortedlist(self):
        print("보고싶은 내역을 선택하세요")
        button = input("1번 - 수입, 2번 - 지출: ")
        if button == "1":
            print("현재까지의 수입 순위")
            sortedlist = sorted(self.income_list, reverse=True)
            for i, amount in enumerate(sortedlist[:10]):
                print(i + 1, "위:", amount, "원")
        elif button == "2":
            print("현재까지 사용한 금액 순위")
            sortedlist = sorted(self.spend_list, reverse=True)
            for i, amount in enumerate(sortedlist[:10]):
                print(i + 1, "위:", amount, "원")
        else:
            print("잘못 입력하셨습니다.")

    # 추가 기능 1: 카테고리별 지출 비율 계산
    def category_spending_ratio(self):
        print("Category Spending Ratios:")
        total_spending = sum(self.spending.values())
        if total_spending == 0:
            print("No spending recorded.")
            return
        for category, amount in self.spending.items():
            ratio = (amount / total_spending) * 100
            print(f"{category}: {ratio:.2f}%")

    # 추가 기능 2: 최근 N개의 거래 내역 조회
    def recent_transactions(self, n):
        print(f"Recent {n} Transactions:")
        for transaction in self.transactions[-n:]:
            if transaction[0] == "Deposit" or transaction[0] == "Initial Balance":
                print(f"{transaction[0]}: +{transaction[1]}원")
            else:
                print(f"{transaction[0]}: -{transaction[1]}원, Category: {transaction[2]}, Description: {transaction[3]}")

    # 추가 기능 3: 예상 잔액 계산
    def projected_balance(self, months):
        average_income = self.income_total / len(self.income_list) if self.income_list else 0
        average_spending = self.spend_total / len(self.spend_list) if self.spend_list else 0
        projected_balance = self.balance + (average_income - average_spending) * months
        print(f"Projected balance after {months} months: {projected_balance}원")

# 가계부 인스턴스 생성
account_book = AccountBook("사용자1", 5000)

# 입출금 기록 및 예산 설정
account_book.deposit(5000)
account_book.set_budget("food", 1000)
account_book.set_budget("entertainment", 500)

account_book.withdraw(300, "편의점에서 음료 구매")
account_book.withdraw(800, "식사 비용")
account_book.withdraw(600, "영화 관람")

# 잔액, 거래 내역, 예산 및 지출 내역 출력
account_book.show_balance()
account_book.show_transactions()
account_book.show_budgets()
account_book.show_spending()
account_book.show_total()
account_book.show_sortedlist()
