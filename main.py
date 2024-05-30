import hashlib
from datetime import datetime

userdata = {}  # 아이디, 비밀번호 저장해둘 딕셔너리
user_registration_dates = {}  # 사용자 등록일 저장
user_accounts = {}  # 사용자별 가계부 데이터 저장

def user_reg():  # 회원가입
    id = input("id 입력: ")  # 회원가입 시의 id 입력
    pw = input("password 입력: ")  # 회원가입 시의 pw 입력

    h = hashlib.sha256()  # hashlib 모듈의 sha256 사용
    h.update(pw.encode())  # sha256으로 암호화
    pw_data = h.hexdigest()  # 16진수로 변환

    userdata[id] = pw_data  # key에 id값을, value에 비밀번호 값
    user_registration_dates[id] = datetime.now()  # 사용자 등록일 저장
    user_accounts[id] = []  # 해당 사용자의 가계부 초기화

    with open('login.txt', 'a', encoding='UTF-8') as fw:  # utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items():  # 딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n')  # key, value값을 차례로 login.txt파일에 저장

    print("환영합니다!")  # 회원가입 성공 메시지 출력

def user_login():  # 로그인
    id = input("id 입력: ")
    pw = input("password 입력: ")

    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    if id in userdata and userdata[id] == pw_data:
        if (datetime.now() - user_registration_dates[id]).total_seconds() < 5:
            print(f"새로운 사용자 {id}님, 환영합니다!")
        else:
            print(f"다시 오신 것을 환영합니다, {id}님!")
        return id
    else:
        print("로그인 실패: 아이디 또는 비밀번호가 잘못되었습니다.")
        return None

def add_income(user_id):
    amount = float(input("수입 금액 입력: "))
    description = input("설명 입력: ")
    user_accounts[user_id].append({"type": "income", "amount": amount, "description": description})

def add_expense(user_id):
    amount = float(input("지출 금액 입력: "))
    description = input("설명 입력: ")
    user_accounts[user_id].append({"type": "expense", "amount": amount, "description": description})

def view_transactions(user_id):
    for transaction in user_accounts[user_id]:
        trans_type = transaction["type"]
        amount = transaction["amount"]
        description = transaction["description"]
        
        if trans_type == "expense" and amount >= 1000:
            print(f"\033[91m{trans_type}: {amount} - {description}\033[0m")
        else:
            print(f"{trans_type}: {amount} - {description}")

b_is_exit = 0
current_user = None

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        user_reg()

    elif func == "2":
        current_user = user_login()

    elif func == "3":
        if current_user:
            print(f"{current_user}님, 현재 로그인 상태입니다.")
            while True:
                print("1. 수입 추가")
                print("2. 지출 추가")
                print("3. 거래 내역 보기")
                print("4. 로그아웃")
                action = input("작업 선택: ")
                if action == "1":
                    add_income(current_user)
                elif action == "2":
                    add_expense(current_user)
                elif action == "3":
                    view_transactions(current_user)
                elif action == "4":
                    print(f"{current_user}님, 로그아웃 되었습니다.")
                    current_user = None
                    break
                else:
                    print("잘못된 입력입니다. 다시 시도하세요.")
        else:
            print("먼저 로그인하세요.")

    elif func == "?":
        print("도움말 입력.")
        print("1: 회원가입")
        print("2: 로그인")
        print("3: 로그인 후 가계부 기능")
        print("?: 도움말")
        print("기타: 종료")

    else:
        b_is_exit = not b_is_exit

