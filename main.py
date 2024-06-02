import hashlib #hashlib 사용
import os
import json
from datetime import datetime, date
import pickle
import Account_book
import random
import webbrowser
import re
import tkinter as tk

""" 
가계부에 필요한 간단한 +-계산기
<단, 연산 기호를 입력하지 않은 상태에서 등호를 누르면 값이 초기화됨>

button_click(key=0) : 숫자 버튼 클릭 시 호출되는 함수
- operator가 'none'이면 num1을 설정
- operator가 설정되어 있으면 num2를 설정

operator_click(op) : 연산자 버튼 클릭 시 호출되는 함수
- operator를 설정

calculate() : 계산 버튼 (=) 클릭 시 호출되는 함수
- 연산자에 따라 계산을 수행
- 연산자가 설정되지 않은 경우 초기화

initialize() :  초기화 버튼 (C) 클릭 시 호출되는 함수
- 모든 변수와 출력 창을 초기화
"""

window = tk.Tk()
window.title('계산기')

operator = 'none'
calculation = 0

def button_click(key=0):
    global num1, num2
    if operator == 'none':
        if print_value.get() == '0':
            print_value.set(str(key))
            num1 = key
        else:
            num1 *= 10
            num1 += key
            print_value.set(str(num1))
    else:
        if print_value.get() == '0' or num2 == 0:
            print_value.set(str(key))
            num2 = key
        else:
            num2 *= 10
            num2 += key
            print_value.set(str(num2))

def operator_click(op):
    global operator
    operator = op

def calculate():
    global num1, num2, operator
    if operator == '+':
        calculation = num1 + num2
    elif operator == '-':
        calculation = num1 - num2
    else:
        calculation = 0

    print_value.set(str(calculation))
    num1 = 0
    num2 = 0
    operator = 'none'

def initialize():
    global num1, num2, operator
    num1 = 0
    num2 = 0
    operator = 'none'
    print_value.set('0')

# 출입력 창
num1, num2 = 0, 0
print_value = tk.StringVar()
print_value.set(0)
display = tk.Entry(window, width=25, textvariable=print_value, justify='right', font=('Arial', 24))
display.grid(columnspan=4, row=0, ipadx=8, ipady=20, sticky='nsew')

# 버튼 크기 조절 및 배치
buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3), ('C', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('+', 2, 4),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('-', 3, 4),
    ('0', 4, 1), ('=', 4, 4)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, command=initialize)
    elif text in '+-':
        button = tk.Button(window, text=text, command=lambda op=text: operator_click(op))
    elif text == '=':
        button = tk.Button(window, text=text, command=calculate)
    else:
        button = tk.Button(window, text=text, command=lambda key=int(text): button_click(key))
    button.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)

# grid 행 및 열 크기 조절
for i in range(1, 5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)



userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

def user_reg():  # 회원가입
    id = input("id 입력: ")
    while True:
        pw = input("password 입력: ")  # 회원가입 시의 pw 입력

        """
        비밀번호 생성 시, 하나 이상의 특수문자가 포함되도록 기능을 추가.
        만약, 특수문자가 포함되지 않는다면 경고문 출력 후 다시 비밀번호 입력을 요구.
        """
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
            print("비밀번호에는 적어도 하나의 특수문자가 포함되어야 합니다.")
            continue

        h = hashlib.sha256()
        h.update(pw.encode())
        pw_data = h.hexdigest()

        userdata[id] = pw_data

        with open('login.txt', 'a', encoding='UTF-8') as fw: #utf-8 변환 후 login.txt에 작성
            for user_id, user_pw in userdata.items(): #딕셔너리 내에 있는 값을 모두 for문
                fw.write(f'{user_id} : {user_pw}\n') #key, value값을 차례로 login.txt파일에 저장
        print("회원가입이 완료되었습니다!")
        break

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

    # 비밀번호 확인
    pw = input("현재 비밀번호 입력: ")
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    if pw_data != userdata2[id_to_modify]['pw']:
        print("비밀번호가 일치하지 않습니다.")
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

class Debt:
    def __init__(self, lender, amount, due_date):
        """
        초기화 함수. 빚의 대출 기관/사람, 금액, 상환 기한을 설정하고 상환된 금액은 0으로 초기화.
        """
        self.lender = lender
        self.amount = amount
        self.due_date = due_date
        self.paid_amount = 0
        self.payment_history = []  # 상환 내역을 저장할 리스트

    def pay_debt(self, amount):
        """
        빚 상환 함수. 상환된 금액을 더하고 남은 빚 금액을 계산하여 반환.
        상환 내역에 기록을 추가.
        """
        self.paid_amount += amount
        self.amount -= amount
        self.payment_history.append((datetime.now(), amount))  # 상환 내역에 추가
        return self.amount

    def get_payment_history(self):
        """
        상환 내역을 반환하는 함수.
        """
        return self.payment_history

debts = []

def validate_date(date_text):
    """
    날짜 형식이 올바른지 확인하는 함수. 'YYYY-MM-DD' 형식이어야 함.
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_debt():
    """
    새로운 빚을 추가하는 함수. 대출 기관/사람, 금액, 상환 기한을 입력받고
    올바른 형식의 상환 기한이 입력될 때까지 반복.
    """
    lender = input("대출 기관/사람: ")
    amount = float(input("대출 금액: "))

    while True:
        due_date = input("상환 기한 (YYYY-MM-DD): ")
        if validate_date(due_date):
            break
        else:
            print("잘못된 날짜 형식입니다. 다시 입력해 주세요.")

    new_debt = Debt(lender, amount, due_date)
    debts.append(new_debt)
    print("새 빚이 추가되었습니다.")

def view_debts():
    """
    등록된 빚 목록을 출력하는 함수. 등록된 빚이 없으면 해당 메시지를 출력.
    """
    if not debts:
        print("등록된 빚이 없습니다.")
    for debt in debts:
        print(f"대출 기관/사람: {debt.lender}, 남은 금액: {debt.amount}, 상환 기한: {debt.due_date}, 상환된 금액: {debt.paid_amount}")

def pay_debt():
    """
    빚 상환 함수. 사용자가 상환할 빚을 선택하고 상환 금액을 입력받아 상환 처리.
    상환 금액이 남은 빚 금액을 초과하지 않도록 검증.
    """
    if not debts:
        print("등록된 빚이 없습니다.")
        return

    # 등록된 빚 목록 출력
    for idx, debt in enumerate(debts):
        print(f"{idx + 1}. 대출 기관/사람: {debt.lender}, 남은 금액: {debt.amount}, 상환 기한: {debt.due_date}, 상환된 금액: {debt.paid_amount}")

    # 상환할 빚 선택
    debt_index = int(input("상환할 빚 번호를 입력하세요: ")) - 1
    selected_debt = debts[debt_index]

    # 상환 금액 입력받아 검증
    while True:
        amount = float(input("상환 금액: "))
        if amount > selected_debt.amount:
            print(f"상환 금액이 남은 빚 금액을 초과할 수 없습니다. 남은 금액: {selected_debt.amount}")
        else:
            break

    # 빚 상환 처리
    remaining_amount = selected_debt.pay_debt(amount)

    # 남은 금액에 따라 메시지 출력
    if remaining_amount <= 0:
        print("모든 빚이 상환되었습니다.")
        debts.pop(debt_index)
    else:
        print(f"남은 금액: {remaining_amount}")

def view_debt_payment_history():
    """
    특정 빚의 상환 내역을 조회하는 함수.
    남아 있는 빚이 있는 경우 상환 내역을 조회 할 수 있다.
    """
    if not debts:
        print("등록된 빚이 없습니다.")
        return

    # 등록된 빚 목록 출력
    for idx, debt in enumerate(debts):
        print(f"{idx + 1}. 대출 기관/사람: {debt.lender}, 남은 금액: {debt.amount}, 상환 기한: {debt.due_date}, 상환된 금액: {debt.paid_amount}")

    # 상환 내역을 조회할 빚 선택
    debt_index = int(input("상환 내역을 조회할 빚 번호를 입력하세요: ")) - 1
    selected_debt = debts[debt_index]

    # 상환 내역 출력
    payment_history = selected_debt.get_payment_history()
    if not payment_history:
        print("상환 내역이 없습니다.")
    else:
        print(f"{selected_debt.lender}의 상환 내역:")
        for date, amount in payment_history:
            print(f"날짜: {date}, 금액: {amount}")

def debt_management():
    """
    빚 관리 기능 함수. 사용자 입력에 따라 빚 추가, 목록 보기, 상환, 상환 내역 조회 기능을 호출.
    """
    while True:
        debt_func = input("빚 관리 기능 입력 (1: 빚 추가, 2: 빚 목록 보기, 3: 빚 상환, 4: 상환 내역 조회, exit: 종료) : ")
        if debt_func == "1":
            add_debt()
        elif debt_func == "2":
            view_debts()
        elif debt_func == "3":
            pay_debt()
        elif debt_func == "4":
            view_debt_payment_history()
        elif debt_func == "exit":
            break
        else:
            print("올바른 기능을 입력해 주세요.")



"""

공동 계정 정보 관리를 위한 JointAccount 클래스
__init__(self, accout_name) : account_name을 공동 계정 이름으로 초기화 및 계정 잔액 0으로 초기화
add_joint_user(self, joint_user) : 공동 계정에 사용자 추가하는 함수
+ joint_users 리스트에 사용자 추가
add_joint_income(self, amount, joint_desc="") : 수입에 관한 거래를 계정에 추가하는 함수
+ 거래 내역 리스트(joint_tran)에 수입 타입, 수입 금액, 설명(메모)이 있는 딕셔너리 추가
+ 잔액에 수입 금액을 더함
add_joint_expense(self, amount, joint_desc="") : 지출에 관한 거래를 계정에 추가하는 함수
+ 거래 내역 리스트(joint_tran)에 지출 타입, 지출 금액, 설명(메모)이 있는 딕셔너리 추가
+ 계정의 잔액에서 지출 금액을 뺌
get_joint_bal(self) : 현재의 잔액을 반환하는 함수
get_joint_tran(self) : 지금까지의 거래 내역 반환하는 함수

"""


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
    with open(expenses_file, 'w', encoding='utf-8') as file:
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
    with open(expenses_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # 새 지출 내역을 리스트에 추가
    data.append(expense)
    # 데이터를 파일에 저장
    with open(expenses_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 저장된 지출 내역을 조회하는 함수
def view_expenses():
    # 파일을 열어 데이터를 불러옴
    with open(expenses_file, 'r', encoding='utf-8') as file:
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
    with open(expenses_file, 'r', encoding='utf-8') as file:
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

# 엔화와 달러의 환율 정보를 정적으로 저장합니다.
exchange_rate = {
    "USD": 0.0009,  # 1달러 = 1100원 (가상의 환율)
    "JPY": 0.1      # 1엔화 = 10원 (가상의 환율)
}

def convert_currency(amount, currency):
    """
    입력된 금액을 선택한 통화로 환전하는 함수
    :param amount: 원화로 입력된 금액
    :param currency: 환전할 통화 (USD 또는 JPY)
    :return: 환전된 금액
    """
    if currency in exchange_rate:
        # 선택한 통화의 환율로 원화를 환전합니다.
        converted_amount = amount * exchange_rate[currency]
        return converted_amount
    else:
        return None

# 환율 계산을 실행하는 부분
def calculate_exchange():
    amount = float(input("환전할 금액(원): "))
    currency = input("환전할 통화를 입력하세요 (USD 또는 JPY): ")
    converted_amount = convert_currency(amount, currency)
    if converted_amount is not None:
        print(f"{amount}원을 {currency}로 환전한 금액은 {converted_amount}입니다.")
    else:
        print("지원되지 않는 통화입니다.")

# 가계부 기능에 환율 계산 추가
def add_entry_with_exchange():
    # 기존의 지출 항목 추가 함수(add_entry())와 비슷하게 작성하되,
    # 추가로 환전할 통화와 금액을 입력받고, 해당 통화로 환전된 금액을 함께 저장합니다.
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    amount = float(input("금액(원): "))
    currency = input("환전할 통화를 입력하세요 (USD 또는 JPY): ")
    converted_amount = convert_currency(amount, currency)
    if converted_amount is not None:
        # 환전된 금액과 통화 정보를 함께 저장합니다.
        entry = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
            "currency": currency,
            "converted_amount": converted_amount
        }
        ledger.append(entry)
        print("항목이 추가되었습니다.")
    else:
        print("지원되지 않는 통화입니다.")

def load_expenses():
    """
    지출 내역을 expenses.json 파일에서 불러오는 함수
    db처럼 지출 정보를 파일에 저장하는 input_expense() 함수를 활용
    """
    try: 
        #expenses.json파일 오픈
        with open('expenses.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"An error occurred while loading expenses: {e}")
        return []

def analyze_and_advise():
    """
    지출 내역을 분석하여 지출을 줄일 수 있는 조언을 제공하는 함수
    """
    expenses = load_expenses()  # 지출 내역을 expenses.json에서 불러옴
    if not expenses: # 저장된 지출이 없음
        print("지출 없음")
        return

    category_totals = {}  # 카테고리 별로 지출 총액을 저장할 딕셔너리
    for expense in expenses:
        category = expense["item"]  # 지출 항목
        amount = float(expense["amount"])  # 문자열로 저장된 금액을 float로 변환
        if category not in category_totals:
            category_totals[category] = 0  # 카테고리가 없으면 초기화
        category_totals[category] += amount  # 카테고리별 지출 금액 합산

    total_expense = sum(category_totals.values())  # 총 지출 금액 계산
    print(f"총 지출: {total_expense} 원")

    advice = []  # 조언을 저장할 리스트
    for category, total in category_totals.items():
        percentage = (total / total_expense) * 100  # 카테고리별 지출 비율 계산
        #비율에 따라 조언 다르게 생성
        if percentage > 30:
            advice.append(f"{category}에서 지출이 총 지출의 {percentage:.2f}%를 차지합니다. {category}에서 절약할 수 있는 방법을 찾아보세요.")
        elif percentage > 20:
            advice.append(f"{category}에서 지출이 총 지출의 {percentage:.2f}%를 차지합니다. 조금 더 신경 써서 지출을 줄여보세요.")

    if advice:
        #조언 출력
        print("지출을 줄일 수 있는 조언:")
        for a in advice:
            print(a)
    else:
        print("지출이 잘 관리되고 있습니다!") #조언이 없을 때

#디데이 기능
d_day_file = 'd_day.json' 

def save_d_day(target_date_str):
    with open(d_day_file, 'w') as file:
        json.dump({"target_date": target_date_str}, file)

def load_d_day():
    if os.path.exists(d_day_file):
        with open(d_day_file, 'r') as file:
            data = json.load(file)
        return data.get("target_date", None)
    return None

def add_d_day():
    try:
        target_date_str = input("디데이 날짜를 입력하세요 (예: 2024-12-31): ")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        today = datetime.today()
        d_day = (target_date - today).days
        if d_day >= 0:
            print(f"D-Day: {d_day}일 남았습니다.")
            save_d_day(target_date_str)
        else:
            print("이미 지난 날짜입니다.")
    except ValueError:
        print("올바른 날짜 형식을 입력하세요 (YYYY-MM-DD).")

def view_d_day():
    target_date_str = load_d_day()
    if target_date_str:
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        today = datetime.today()
        d_day = (target_date - today).days
        if d_day >= 0:
            print(f"D-Day: {d_day}일 남았습니다.")
        else:
            print("이미 지난 디데이입니다.")
    else:
        print("저장된 디데이 정보가 없습니다.")

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