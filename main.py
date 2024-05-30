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


# 아이디와 전화번호를 입력 받아 비밀번호를 찾는 함수
def find_pw_by_id_phone():
    id = input("ID 입력: ")  # 사용자로부터 ID 입력 받음
    phone = input("전화번호 입력: ")  # 사용자로부터 전화번호 입력 받음
    
    # 입력받은 ID와 전화번호가 일치하는 지 확인
    if id in userdata2 and userdata2[id]['phone'] == phone:
        # 일치하는 경우 암호화된 비밀번호 출력
        print(f"비밀번호 (암호화된 형태): {userdata2[id]['pw']}")
    else:
        # 정보가 일치하지 않는 경우 메시지 출력
        print("일치하는 사용자 정보를 찾을 수 없습니다.")

# 전체 회원 목록을 출력하는 함수
def print_all_users():
    print("전체 회원 목록:")
    for user_id, user_info in userdata2.items():
        # 각 회원의 ID, 이름, 전화번호 출력
        print(f"ID: {user_id}, 이름: {user_info['name']}, 전화번호: {user_info['phone']}")

# 회원의 아이디로 회원의 이름과 전화번호를 찾는 함수
def find_name_phone_by_id():
    id = input("ID 입력: ")  # 사용자로부터 ID 입력 받음
    
    if id in userdata2:
        # 해당 ID를 가진 사용자의 이름과 전화번호 출력
        print(f"이름: {userdata2[id]['name']}, 전화번호: {userdata2[id]['phone']}")
    else:
        # ID가 일치하는 사용자를 찾을 수 없는 경우 메시지 출력
        print("해당 ID를 가진 사용자를 찾을 수 없습니다.")


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