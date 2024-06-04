import hashlib #hashlib 사용
import os
import json
from datetime import datetime, date
import pickle
import Account_book
import random
import webbrowser
import re
import Add_function

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

    # 전화번호 중복 체크
    # 중복된 전화번호를 입력한 경우 다른 전화번호를 입력하도록 설정
    while phone in userphones:
        print("이미 등록된 전화번호입니다. 다른 전화번호를 입력해주세요.")
        print("( 만약 입력한 전화번호로 등록된 id를 찾고 싶은 경우 ?를 입력하시오 )")
        phone = input("전화번호 입력: ")
        if phone == '?' : # 전화번호로 등록된 id를 찾고 싶은 경우
            find_id_by_phone()
            print("로그인 기능으로 다시 돌아갑니다.")
            return #로그인 기능으로 다시 돌려줌

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

"""
add_memo : 파일 입출력을 사용하여 메모장을 추가할 수 있는 기능으로 예상지출내역, 오늘의 목표등을 기록할 수 있다.
@Parm
    None
@Return
    None
"""

memo_directory = []
def add_memo():
    print("메모장 제목: ")
    str_title = input()
    if not str_title.endswith(".txt"):
        str_title += ".txt"
    if '/' in str_title:
        print("메모장 제목에 경로 정보가 포함되었습니다.")
    try:
        # 디렉토리 경로 추출
        directory = os.path.dirname(str_title)

        # 디렉토리가 존재하지 않으면 생성
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # 파일 열기
        with open(str_title, "w", encoding="utf8") as new_f:
            # 파일에 쓸 내용을 입력 받음
            content = input("메모할 내용을 입력하세요: ")
            new_f.write(content)
            new_f.close()
            print("메모가 성공적으로 저장되었습니다.")
            if directory not in memo_directory :
                memo_directory.append(directory)
                print("새로운 메모 디렉토리가 추가되었습니다.")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: '{str_title}'")
    except PermissionError:
        print(f"파일을 생성할 권한이 없습니다: '{str_title}'")
    except Exception as e:
        print(f"다른 오류가 발생했습니다: {e}")

def list_memo():
    """
    현재 디렉토리에 있는 메모장 파일 리스트를 출력하는 함수
    """
    memo_files = []
    for directory in memo_directory:
        try:
            # 지정된 디렉토리에서 파일 목록을 가져옴
            for file in os.listdir(directory):
                if file.endswith(".txt"):
                    # 전체 파일 경로를 구성하여 리스트에 추가
                    memo_files.append(os.path.join(directory, file))
        except FileNotFoundError:
            print(f"디렉토리를 찾을 수 없습니다: '{directory}'")
        except PermissionError:
            print(f"디렉토리에 대한 접근 권한이 없습니다: '{directory}'")
        except Exception as e:
            print(f"다른 오류가 발생했습니다: {e}")
    if memo_files:
        print("메모장 목록:")
        for idx, memo_file in enumerate(memo_files, start=1):
            print(f"{idx}. {memo_file}")
    else:
        print("메모장이 존재하지 않습니다.")

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
    while True:
        print("-----------------------")
        print("user:",user.name) # 현재 user가 누구인지 출력
        print("""
        1: 메모 추가
        2: 메모 리스트
        3. 메모 읽기
        4. 메모 삭제
        5. 메모 닫기
        """)
        choice = input("선택: ")
        if choice == "1":
            add_memo()
        elif choice == "2":
            list_memo()
        elif choice == "3":
            read_memo()
        elif choice == "4":
            delete_memo()
        elif choice == "5":
            break
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

def filter_expenses_by_date(start_date, end_date):
    """
    특정 기간 동안의 지출 내역을 필터링하여 출력합니다.
    @param start_date : 문자열 형식의 시작 날짜 (YYYY-MM-DD).
    @param end_date : 문자열 형식의 종료 날짜 (YYYY-MM-DD).
    """
    for entry in ledger:
        if start_date <= entry['date'] <= end_date:
            print(entry)

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

    category_count = sum(1 for e in ledger if e["category"] == category)

    if category_count >= 3 and category not in favorites: #같은 카테고리가 3번 이상 입력되면 즐겨찾기에 추가할 것인지 알람창을 출력.
        response = input(f"'{category}' 같은 카테고리가 3회 이상 입력되었습니다. 즐겨찾기에 추가하시겠습니까? ('y' or 'n'): ").strip().lower()
        if response == 'y': #'y'입력시, 카테고리를 즐겨찾기 항목에 추가.
            add_favorite_category(category)
        else:
            print("카테고리에 추가되지 않았습니다.")


favorites = []

def add_favorite_category(category): #즐겨찾기 항목에 추가.
    if category not in favorites:  #카테고리가 즐겨찾기에 존재하지 않는다면, 즐겨찾기 추가. 그렇지 않다면, 경고창 출력.
        favorites.append(category)
        print(f"'{category}' 카테고리가 즐겨찾기에 추가되었습니다.")
    else:
        print(f"'{category}' 카테고리는 이미 즐겨찾기에 있습니다.")

def show_favorites():
    if not favorites:
        print("즐겨찾기 카테고리 목록이 비어 있습니다.")
    else:
        print("즐겨찾는 카테고리 목록:")
        for category in favorites:
            print(f"- {category}")

# 항목 조회 함수
def view_entries():
    for entry in ledger:
        print(entry)
        if "score" in entry:
            print(f"평가 점수: {entry['score']}")


def day_evaluation():
    # 사용자로부터 그날의 평가를 입력 받음
    while True:     #잘못된 값 입력 시 다시 입력 받을 수 있도록 수정 
        evaluation = input("오늘의 평가를 입력하세요 (0에서 10까지): ")
        try:
            evaluation = float(evaluation)
            if 0 <= evaluation <= 10:
                print(f"오늘의 평가는 {evaluation}점입니다.")
                return evaluation
            else:
                print("평가는 0에서 10 사이의 숫자여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def calculate_average_score(scores):
    if scores:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        return average_score
    else:
        return None

def recommend_financial_product(products):
    # 사용자에게 입력 받은 여러 금융 상품 정보를 비교하여 가장 유리한 상품을 추천
    # 이 함수는 각 상품의 이자율, 수수료 등을 비교하여 최적의 상품을 찾아냅니다.
    # 이 코드는 사용자에게서 각 상품의 정보를 입력받는 것을 가정하고, 실제 데이터베이스나 외부 API로부터 데이터를 가져올 수도 있습니다.
    best_product = None
    best_interest_rate = 0
    lowest_fee = float('inf')

    for product in products:
        interest_rate = product['interest_rate']
        fee = product['fee']

        # 이자율이 높고 수수료가 낮은 상품을 찾음
        if interest_rate > best_interest_rate and fee < lowest_fee:
            best_product = product
            best_interest_rate = interest_rate
            lowest_fee = fee

    return best_product

def get_products_from_user():
    products = []
    while True:
        product_info = {}
        product_info['interest_rate'] = float(input("금융 상품의 이자율을 입력하세요: "))
        product_info['fee'] = float(input("금융 상품의 수수료를 입력하세요: "))
        products.append(product_info)
        more_products = input("더 입력하시겠습니까? (Y/N): ")
        if more_products.lower() != 'y':
            break
    return products

def average():
    나이 = input("나이 입력: ")
    나이 = int(나이)

    if 나이 >= 20 and 나이 < 30:
        print("한달 평균 생활비는 136.2만원 입니다.")
    elif 나이 >= 30 and 나이 < 40:
        print("한달 평균 생활비는 246.3만원 입니다.")
    elif 나이 >= 40 and 나이 < 50:
        print("한달 평균 생활비는 286만원 입니다.")
    elif 나이 >= 50 and 나이 < 60:
        print("한달 평균 생활비는 244만원 입니다.")
    elif 나이 >= 60:
        print("한달 평균 생활비는 148.9만원 입니다.")
    else:
        print("올바른 나이를 입력하십시오")
"""   
나이를 입력받고 한국 1인 평균  생활비를 보여주는 기능    
"""     

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

def sort_entries_by_date():
    """
    지출 내역을 날짜순으로 정렬하여 출력하는 함수
    """
    if not ledger:
        print("저장된 지출 내역이 없습니다.")
        return

    sorted_entries = sorted(ledger, key=lambda x: x['date'])
    print("지출 내역 (날짜순):")
    for entry in sorted_entries:
        print(entry)

def sort_entries_by_amount():
    """
    지출 내역을 금액순으로 정렬하여 출력하는 함수
    """
    if not ledger:
        print("저장된 지출 내역이 없습니다.")
        return

    sorted_entries = sorted(ledger, key=lambda x: x['amount'])
    print("지출 내역 (금액순):")
    for entry in sorted_entries:
        print(entry)


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

def init_Account_book(num): #가계부 하나의 모든기록 초기화(기존의 이름과 새로 입력받은 잔액으로 초기화), choose_Account와 연동 - 2
    if(num < 0):#오류 검출
      print("잘못 입력하셨습니다.(0이하수 입력)")
    else:
      bal = input("남기고 싶은 잔액을 입력하세요. (x 입력시 현재잔액을 입력)") #주의 - 잔액 설정시 char형으로 저장 -> int형으로 변환해야 함
      if(bal == "x"):
        print("잔액을 그대로 가져옵니다.")
        bal = Account_list[num-1].bal
      else:
        if(bal.isnumeric()): #숫자를 표현하는지 확인
          bal = int(bal) 
        else:
          print("잘못 입력하셨습니다.(잔액 이상)")
          return 0
      print(f"가계부 {num}번을 초기화 합니다.")
      name = Account_list[num-1].name #원래 저장소에서 이름 가져오기(배열은 0~n-1로 이루어짐)
      Account_list[num-1] = Account_book(name,bal) #새로운 객체 생성 -> 기존 리스트에서 교체
      print(f"가계부 {num}번이 이름: {Account_list[num-1].name}과 잔액: {Account_list[num-1].bal}으로 초기화 되었습니다.")

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

def print_Login_help(): #user interface 도움말
    print("""
    1: 회원가입
    2: 로그인
    3. 아이디 찾기
    4. 비밀번호 찾기
    
    아무거나 입력시 프로그램 종료
    
    ?: 로그인 도움말 출력
    """)

def read_user_information(): #login.txt에서 읽어온 후 dic에 저장
    #파일 읽어 오기
    f = open("login.txt",'r',encoding='UTF-8')

    login_info = []#파일 정보 저장
    #한줄씩 읽어 온 후 리스트에 저장
    while True:
        line = f.readline()
        if line == '':
            break
        line = line.replace(' ','')#필요없는 값 삭제
        line = line.replace('\n','')
        line = line.split(':')
        #파일에서 딕셔너리로 복구 시켜주는 코드(userdata2, usernames, userphones를 복구시킴)
        login_info.append(line)
        userdata2[line[0]] = {'pw': line[1], 'name': line[2], 'phone': line[3]} 
        usernames[line[2]] = line[0]
        userphones[line[3]] = line[0] 
    f.close()
    return login_info #파일의 모든 정보가 저장된 리스트 반환 - 이후 로그인 인터페이스에서 사용을 위함

def Login_interface(): #로그인 인터페이스
    login_info = read_user_information() #주의 - read_user_information()이 항상 위에 있어야함(인터프리터 방식)
    if len(login_info)==0 : 
        print("로그인 정보가 없습니다.\n회원가입을 진행해주세요.")
        return 0
    elif login_info is None : 
        print("오류가 발생했습니다.")
        return 0
    print("로그인(ID와 PW를 입력해 주세요.)")
    ID = input("ID: ")
    PW = input("PW: ")

    h = hashlib.sha256()

    # 파일 읽기 관련 예외 처리
    try:
        with open("login.txt", "r", encoding="UTF-8") as f:
            login_info = [line.strip().split(":") for line in f.readlines()]
    except FileNotFoundError:
        print("로그인 정보 파일을 찾을 수 없습니다.")
        return 0
    except Exception as e:
        print(f"로그인 정보를 읽는 도중 오류가 발생했습니다: {e}")
        return 0
    
    cnt = 0

    login_info = read_user_information() #주의 - read_user_information()이 항상 위에 있어야함(인터프리터 방식)

    for i in range(len(login_info)):
        if(login_info[i][0] == ID):
            h.update(PW.encode()) #문자열로 비밀번호 추가 가능
            login_pw = h.hexdigest()#암호화 후 출력

            if(login_info[i][1] == login_pw): #ID가 맞으면 PW 확인
                print(f"환영합니다. {login_info[i][2]} 고객님")#맞으면 이름 출력
                return User(login_info[i][2]) #user 객체 반환 - 이후 user정보에 입력 위함
            else:
                print("비밀번호 오류입니다.")#아니면 끝
                break
        cnt += 1

    if(cnt == len(login_info)): # cnt로 리스트의 끝인지 check
        print("존재하지 않는 아이디입니다.")
    return 0

def change_pw_by_phone(): #ID와 전화번호 또는 ID와 이름으로 pw변경 - find_id_by_phone()에서 이름 또한 포함되도록 변경
    check = 0

    ID = input("찾고자 하는 사용자의 ID 입력: ")  # 사용자가 찾고자 하는 ID를 입력받음

    if ID in userdata2:  # ID(key)가 딕셔너리에 존재하는지 확인
        print(f"{userdata2[ID]['name']}님, 전화번호를 입력해 주십시오.")
        phone = input("전화번호 입력: ")

        if phone in userphones:
            while(True):#비밀번호를 바꿀때 까지 무한루프
                P = input("사용하고자 하는 비밀번호를 입력해 주십시오: ")
                check = input(f"사용하고자 하는 비밀번호가 {P}가 맞나요?(맞으면 1, 아니면 아무거나 입력): ")

                if(check == "1"): #주의 - check는 input으로 받으므로 char 형임
                    h = hashlib.sha256() #암호 복호화
                    h.update(P.encode())
                    P = h.hexdigest()

                    userdata2[ID]['pw'] = P#dic 수정

                    with open('login.txt', 'w', encoding='UTF-8') as fw:  # utf-8 변환 후 login.txt에 작성
                        for user_id, user_info in userdata2.items():
                            fw.write(f'{user_id} : {user_info["pw"]} : {user_info["name"]} : {user_info["phone"]}\n')  # 아이디, 비밀번호, 이름, 전화번호 값을 차례로 login.txt파일에 저장
                    break

        else:
            print("해당 전화번호를 가진 사용자가 없습니다. 다시 입력해 주십시오") #전화번호 존재 X
    else:
        print("ID가 존재하지 않습니다.") #ID 존재 X

YU_Account() #프로그램 시작 화면

version = "1.0.0"  # 프로그램 버전
print(f"프로그램 버전: {version}")

#########################################################
# 사용자로부터 날짜를 입력받는 함수입니다.
# 문자열을 datetime 객체로 변환합니다.
# 올바른 날짜 형식이면 변환된 datetime 객체를 반환합니다.
# 날짜 형식이 잘못된 경우 안내 메시지를 출력하고 다시 입력을 요청합니다.
def input_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("올바른 날짜 형식이 아닙니다. YYYY-MM-DD 형식으로 입력하세요.")

# 재정 목표를 나타내는 클래스입니다.
"""
        재정 목표 객체를 초기화합니다.
        Args:
            목표의 이름, 목표의 금액, 목표의 달성 기한을 설정하고, 현재까지의 저축금액을 0으로 초기화
"""
class FinancialGoal:
    def __init__(self, name, target_amount, due_date):
        self.name = name
        self.target_amount = target_amount
        self.due_date = due_date
        self.saved_amount = 0

    # 목표에 저축 금액을 추가하는 메서드입니다.
    # 목표의 현재 저축 금액에 입력된 금액을 더합니다.
     # 추가된 저축 금액을 안내합니다.
    def add_savings(self, amount):
        self.saved_amount += amount
        print(f"{amount}원이 목표에 추가되었습니다. 현재 저축액: {self.saved_amount}원")

    # 목표의 진행 상황을 확인하는 메서드입니다.
    # 남은 금액과 남은 일 수를 계산하고, 목표를 달성했다면 달성했음을 알리고 목표한 금액과 현재 저축 상태를 출력합니다.
    # 목표를 달성하지 않았다면 목표 금액과 현재 저축 상태와 남은 금액, 남은기간을 출력합니다.
    def check_progress(self):
        remaining_amount = self.target_amount - self.saved_amount
        days_left = (self.due_date - datetime.now()).days
        if remaining_amount <= 0:
            print(f"축하합니다! '{self.name}' 목표를 달성했습니다! \n 목표 금액: {self.target_amount}원\n현재 저축액: {self.saved_amount}원\n")
        else:
            print(f"목표: {self.name}\n목표 금액: {self.target_amount}원\n현재 저축액: {self.saved_amount}원\n남은 금액: {remaining_amount}원\n남은 기간: {days_left}일")


# 사용자 정보를 담는 클래스입니다.
# 사용자의 이름을 설정하고, 사용자의 재정 목표 리스트를 빈 리스트로 초기화합니다.
class User:
    def __init__(self, name):
        self.name = name
        self.goals = []


    # 목표 리스트에서 특정 인덱스의 목표를 가져오는 메서드입니다.
    #해당 인덱스의 목표 객체를 반환하거나, 인덱스가 올바르지 않을 경우 None을 반환합니다.
    def get_goal(self, index):
        if 0 <= index < len(self.goals):
            return self.goals[index]
        else:
            return None

# 재정 목표를 관리하는 루프 함수입니다.
def financial_goal_loop(user):
    while True:
        print("\n--- 재정 목표 관리 ---")
        print("1: 새로운 목표 추가")
        print("2: 목표 목록 확인")
        print("3: 목표 저축액 추가")
        print("4: 목표 진행 상황 확인")
        print("0: 메인 메뉴로 돌아가기")

        # 사용자로부터 기능 선택을 입력받습니다.
        choice = input("기능을 선택하세요: ")
          # 새로운 목표를 추가하는 기능입니다.
        if choice == "1":
            name = input("목표 이름을 입력하세요: ")
            target_amount = int(input("목표 금액을 입력하세요: "))
            due_date = input_date("목표 달성 기한을 입력하세요 (YYYY-MM-DD): ")
            user.goals.append(FinancialGoal(name, target_amount, due_date))
            print("새로운 목표가 추가되었습니다.")
        # 목표 목록을 확인하는 기능입니다.
        elif choice == "2":
            if not user.goals:
                print("등록된 목표가 없습니다.")
            else:
                print("등록된 목표 목록:")
                for idx, goal in enumerate(user.goals, start=1):
                    print(f"{idx}: {goal.name}")
        # 등록된 목표를 나타내고 사용자에게 특정한 목표를 입력받아 저축앨을 추가하는 기능입니다.
        elif choice == "3":
            if not user.goals:
                print("등록된 목표가 없습니다. 먼저 목표를 추가하세요.")
            else:
                print("등록된 목표 목록:")
                for idx, goal in enumerate(user.goals, start=1):
                    print(f"{idx}: {goal.name}")
                goal_index = int(input("저축액을 추가할 목표를 선택하세요: ")) - 1
                selected_goal = user.get_goal(goal_index)
                if selected_goal:
                    amount = int(input("추가할 저축액을 입력하세요: "))
                    selected_goal.add_savings(amount)
                else:
                    print("올바른 목표를 선택하세요.")
        #목표 목록을 출력하고, 사용자에게 특정한 목표를 입력받아 해당 목표의 진행 상황을 확인하는 기능입니다.
        #목표한 금액을 모두 모았다면 목표했던 금액과 현재 저축액을 출력합니다.
        #목표 목록에 없는 번호 입력시 사용자에게 다시 입력 받습니다.
        elif choice == "4":
            if not user.goals:
                print("등록된 목표가 없습니다. 먼저 목표를 추가하세요.")
            else:
                print("등록된 목표 목록:")
                for idx, goal in enumerate(user.goals, start=1):
                    print(f"{idx}: {goal.name}")
                goal_index = int(input("진행 상황을 확인할 목표를 선택하세요: ")) - 1
                selected_goal = user.get_goal(goal_index)
                if selected_goal:
                    selected_goal.check_progress()
                else:
                    print("올바른 목표를 선택하세요.")
        #메인 메뉴로 돌아가는 기능입니다.
        elif choice == "0":
            print("메인 메뉴로 돌아갑니다.")
            break
        #재정 목표 관리 반복문에 없는 번호 입력시 사용자에게 다시 입력 받습니다.
        else:
            print("올바른 기능을 선택하세요.")






import datetime

 # 투자 종류, 투자 이름, 투자한 금액, 투자한 날짜, 현재 투자가치에 대하여 정의
class Investment:
    def __init__(self, type, name, amount_invested, date_invested, current_value):
        self.type = type
        self.name = name
        self.amount_invested = amount_invested
        self.date_invested = date_invested
        self.current_value = current_value
   
    #투자의 손익값 계산 (현재 가치 - 투자 금액)
    def profit_loss(self):
        return self.current_value - self.amount_invested
    #투자의 손익률 계산 ((손익 / 투자 금액) * 100)
    def profit_loss_percentage(self):
        return (self.profit_loss() / self.amount_invested) * 100
# 투자 내역을 저장하는 리스트
investment_list = []

# 날짜 입력을 받는 함수
# 빈칸을 입력하면 None 반환
def input_date(prompt):
    while True:
        date_str = input(prompt)
        if date_str.strip() == "":
            return None
        try: # 입력된 날짜 문자열을 datetime 객체로 변환
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj
        except ValueError: # 날짜 형식이 올바르지 않은 경우 출력
            print("올바른 날짜 형식을 입력해 주세요. (YYYY-MM-DD)")

# 금액 입력을 받는 함수
# 빈칸을 입력하면 None 반환
def input_amount(prompt):
    while True:
        amount_str = input(prompt)
        if amount_str.strip() == "":
            return None
        try:# 입력된 금액 문자열을 float로 변환
            amount = float(amount_str)
            return amount
        except ValueError: # 금액 형식이 올바르지 않은 경우 출력
            print("올바른 금액을 입력해 주세요. 숫자 형식으로 입력하세요.")

# 새로운 투자 내역을 추가하는 함수
def add_investment():
    type = input("투자 종류 (주식, 펀드, 암호화폐 등): ")
    name = input("투자 이름: ")
    amount_invested = input_amount("투자 금액: ")
    date_invested = input_date("투자 날짜 (YYYY-MM-DD): ")
    current_value = input_amount("현재 가치: ")

     # 입력받은 정보를 사용하여 Investment 객체 생성
     # 생성된 Investment 객체를 리스트에 추가
    investment = Investment(type, name, amount_invested, date_invested, current_value)
    investment_list.append(investment)
    print("투자 내역이 추가되었습니다.")

# 모든 투자 내역을 조회하는 함수
def view_investments():
    for idx, investment in enumerate(investment_list, start=1):
        print(f"{idx}. {investment.type} - {investment.name}")
        print(f"   투자 금액: {investment.amount_invested} 원")
        print(f"   투자 날짜: {investment.date_invested.strftime('%Y-%m-%d')}")
        print(f"   현재 가치: {investment.current_value} 원")
        print(f"   손익: {investment.profit_loss()} 원 ({investment.profit_loss_percentage():.2f}%)")
        print("-----------------------------")

# 투자 내역을 수정하는 함수
# 빈 문자열이 아니면 입력한 값으로, 아니면 기존 값으로 설정합니다.
def update_investment():
    view_investments()
     # 현재 투자 내역을 조회합니다.
    idx = int(input("수정할 투자 내역 번호: ")) - 1
     # 선택된 투자 내역을 가져옵니다.
      # 입력된 번호가 유효한 범위 내에 있는지 확인합니다.
    if 0 <= idx < len(investment_list):
        investment = investment_list[idx]
        print("수정할 내용을 입력하세요. (빈칸으로 두면 변경되지 않습니다.)")
        type = input(f"투자 종류 ({investment.type}): ") or investment.type
        name = input(f"투자 이름 ({investment.name}): ") or investment.name
        amount_invested = input_amount(f"투자 금액 ({investment.amount_invested}): ")
        amount_invested = amount_invested if amount_invested is not None else investment.amount_invested
        date_invested = input_date(f"투자 날짜 ({investment.date_invested.strftime('%Y-%m-%d')}): ")
        date_invested = date_invested if date_invested is not None else investment.date_invested
        current_value = input_amount(f"현재 가치 ({investment.current_value}): ")
         # 빈 문자열이 아니면 입력한 값으로, 아니면 기존 값으로 설정합니다.
        current_value = current_value if current_value is not None else investment.current_value
        
         # 수정된 정보를 반영하여 Investment 객체 갱신
        investment.type = type
        investment.name = name
        investment.amount_invested = amount_invested
        investment.date_invested = date_invested
        investment.current_value = current_value
        print("투자 내역이 수정되었습니다.")
    else: # 잘못된 번호가 입력된 경우 오류 메시지를 출력합니다.
        print("올바른 번호를 입력해 주세요.")

# 투자 내역을 삭제하는 함수
# 리스트에서 해당 투자 내역 삭제
def delete_investment():
    view_investments()
    idx = int(input("삭제할 투자 내역 번호: ")) - 1
    if 0 <= idx < len(investment_list):
        investment_list.pop(idx)
        print("투자 내역이 삭제되었습니다.")
    else:
        print("올바른 번호를 입력해 주세요.")
# 투자 추적 기능 루프
def investment_tracker():
    while True:
        print("-----------------------")
        print("투자 추적 기능")
        print("1. 투자 내역 추가")
        print("2. 투자 내역 조회")
        print("3. 투자 내역 수정")
        print("4. 투자 내역 삭제")
        print("5. 돌아가기")
        choice = input("선택: ")
        
        if choice == "1":
            add_investment()
        elif choice == "2":
            view_investments()
        elif choice == "3":
            update_investment()
        elif choice == "4":
            delete_investment()
        elif choice == "5":
            break
        else:
            print("올바른 선택을 해주세요.")












# 프로그램 종료 여부를 판단하는 변수
b_is_exit = 0
interface = 0 #인터페이스 만들기
user = 0 #user 이름 저장 변수

while user == 0: #유저 입력할때 까지 무한루프 도는 인터페이스 구현(탈출을 원할 시 0)
    interface = input("로그인 기능 입력 (? 입력시 도움말) : ")

    if interface == "1":
        user_reg_include_name_phone() #회원가입 함수 - 이미 존재
    elif interface == "2":
        user = Login_interface()#유저 상태를 user 변수에 저장 - 이후 기능 사용시 user에 해당하는 자료에서 산출
    elif interface == "3":
        find_id_by_phone() #id 찾기 - 이미 존재
    elif interface == "4": 
        change_pw_by_phone() #pw 찾기 - id 찾기 함수 변형
    elif interface == "?":
        print_Login_help() #?입력시 Login 도움말 띄우기
    else:
        print("프로그램을 종료합니다.")
        user = interface
        b_is_exit = 1


# 메인 루프
while not b_is_exit:
    print("-----------------------")
    print("user:",user.name) # 현재 user가 누구인지 출력
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
        investment_tracker()

    elif func == "?":
        print_help()
    elif func == "exit" or func == "x" or func =="종료":
        print("프로그램을 종료합니다.")
        b_is_exit = True
    elif func == "memo":
        add_memo()
        memo()
    else:
        
        print("올바른 기능을 입력해 주세요.")