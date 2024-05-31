import hashlib  # hashlib 모듈을 사용하여 비밀번호 암호화를 처리
import os  # 파일 입출력 및 경로 조작을 위해 os 모듈을 사용
import json  # json 파일 입출력을 위해 json 모듈을 사용
from datetime import datetime  # 날짜 및 시간을 처리하기 위해 datetime 모듈을 사용
import pickle  # 객체를 파일에 저장하고 불러오기 위해 pickle 모듈을 사용
import webbrowser  # 웹 브라우저를 열기 위해 webbrowser 모듈을 사용
from Account_book import Account_book  # Account_book 클래스를 사용하기 위해 모듈을 가져옴

# 사용자 데이터를 저장할 딕셔너리 초기화
userdata = {}

# 회원가입 함수
def user_reg():
    # 사용자로부터 아이디와 비밀번호 입력받음
    id = input("id 입력: ")
    pw = input("password 입력: ")

    # 비밀번호를 SHA-256으로 해시 처리
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    # 'login.txt' 파일을 바이너리 쓰기 모드로 열기
    f = open('login.txt', 'wb')

    # 사용자 데이터를 딕셔너리에 저장
    userdata[id] = pw_data

    # 'login.txt' 파일에 사용자 데이터를 UTF-8로 인코딩하여 저장
    with open('login.txt', 'a', encoding='UTF-8') as fw:
        for user_id, user_pw in userdata.items():
            fw.write(f'{user_id} : {user_pw}\n')

# 지출 기록 함수
def day_spending(hist, spending, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    # 기록할 날짜 및 시간 설정
    dt = datetime(year, month, day, hour)
    # 해당 날짜에 지출 기록이 없으면 리스트 초기화
    if f"{dt}" not in hist:
        hist[f"{dt}"] = []
    # 지출 내역을 리스트에 추가
    hist[f"{dt}"].append((-spending, where))

# 수입 기록 함수
def day_income(hist, income, where="", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour):
    # 기록할 날짜 및 시간 설정
    dt = datetime(year, month, day, hour)
    # 해당 날짜에 수입 기록이 없으면 리스트 초기화
    if f"{dt}" not in hist:
        hist[f"{dt}"] = []
    # 수입 내역을 리스트에 추가
    hist[f"{dt}"].append((income, where))

# 새 계정 생성 함수
def new_account(user_id, bal):
    # 가계부 초기 데이터 설정
    household_ledger = {'user_id': user_id, 'bal': bal, 'history': {}}
    # 사용자 이름으로 된 파일에 데이터를 저장
    with open(f'{user_id}.txt', 'wb') as info:
        pickle.dump(household_ledger, info)

# 계정 정보 열기 함수
def open_account_info(user_id):
    try:
        # 사용자 이름으로 된 파일을 열어 데이터 로드
        with open(f'{user_id}.txt', 'rb') as info:
            user_dict = pickle.load(info)
        return user_dict
    except Exception as e:
        print(f"{user_id}의 정보를 불러오는 과정에서 오류가 발생하였습니다. : {e}")
        return None

# 계산기 함수
def calculator():
    try:
        # 사용자로부터 계산할 수식을 입력받음
        expr = input("계산할 수식을 입력하세요 (예: 2 + 3 * 4): ")
        # 입력된 수식을 평가하여 결과를 계산
        result = eval(expr)
        print(f"결과: {result}")
    except Exception as e:
        print(f"오류 발생: {e}")

# 가계부 데이터를 저장할 리스트 초기화
ledger = []

# 도움말 출력 함수
def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 월별 보고서 생성
    4: 예산 설정 및 초과 알림
    5: 지출 카테고리 분석
    6: 가계부 작성법 사이트 열기
    7: 모든 데이터 초기화
    ?: 도움말 출력
    exit: 종료
    메모장: 메모 작성
    """)

# 수입/지출 항목 추가 함수
def add_entry():
    # 사용자로부터 항목 정보를 입력받음
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    amount = float(input("금액: "))
    # 항목 데이터를 딕셔너리로 저장
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
    # 저장된 모든 항목을 출력
    for entry in ledger:
        print(entry)

# 월별 보고서 생성 함수
def generate_monthly_report():
    # 사용자로부터 보고서 생성할 월을 입력받음
    month = input("보고서 생성할 월 (YYYY-MM): ")
    monthly_total = 0
    # 입력받은 월에 해당하는 항목들을 조회하고 합산
    for entry in ledger:
        if entry["date"].startswith(month):
            monthly_total += entry["amount"]
            print(entry)
    print(f"{month}월 총 지출: {monthly_total} 원")

# 예산 설정 및 초과 알림 함수
def set_budget():
    # 사용자로부터 예산을 입력받음
    budget = float(input("예산 설정 (원): "))
    current_total = sum(entry["amount"] for entry in ledger)
    # 현재 지출이 예산을 초과했는지 확인하고 알림
    if current_total > budget:
        print(f"경고: 예산 초과! 현재 지출: {current_total} 원")
    else:
        print(f"예산 설정 완료. 현재 지출: {current_total} 원, 남은 예산: {budget - current_total} 원")

# 지출 카테고리 분석 함수
def analyze_categories():
    # 각 카테고리별 지출 합계를 계산
    category_totals = {}
    for entry in ledger:
        category = entry["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += entry["amount"]
    # 각 카테고리별 지출 합계를 출력
    for category, total in category_totals.items():
        print(f"{category}: {total} 원")

# 메모 작성 함수
def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title, "w", encoding="utf8")
    print("내용 입력: ")
    str_memo = input()
    new_f.write(str_memo)
    new_f.close()

# 가계부 작성법 사이트 열기 함수
def open_guide():
    url = "https://blog.naver.com/mkjang0202/222983209628?viewType=pc"  # 여기에 가계부 작성법 사이트의 URL을 입력하세요
    webbrowser.open(url)
    print("가계부 작성법 사이트를 열었습니다.")

# 모든 데이터 초기화 함수
def reset_data():
    global ledger
    confirm = input("모든 데이터를 초기화하시겠습니까? (yes 입력 시 초기화): ")
    if confirm.lower() == 'yes':
        ledger = []
        if os.path.exists(expenses_file):
            os.remove(expenses_file)
        with open(expenses_file, 'w') as file:
            json.dump([], file)
        print("모든 데이터가 초기화되었습니다.")
    else:
        print("데이터 초기화가 취소되었습니다.")

# 지출 내역을 저장할 파일 이름 설정
expenses_file = 'expenses.json'

# 프로그램 시작 시 파일이 존재하지 않으면 초기화
if not os.path.exists(expenses_file):
    with open(expenses_file, 'w') as file:
        json.dump([], file)

# 지출 내역 저장 함수
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

# 가계부 초깃값 임의로 설정
a = Account_book("가계부 1", 1000000)
b = Account_book("가계부 2", 2000000)
c = Account_book("가계부 3", 3000000)

# 가계부 리스트
Account_list = [a, b, c]

# 가계부 선택 함수
def choose_Account(func):
    print("가계부 선택(번호로 입력)")
    for i in range(0, len(Account_list)):
        print(f"가계부 {i+1}번 : ", Account_list[i].name)
    choose = input()
    return choose

# 프로그램 종료 여부를 판단하는 변수 초기화
b_is_exit = 0

# 메인 루프
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    # 입력된 기능에 따라 함수를 호출
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
        open_guide()
    elif func == "7":
        reset_data()
    elif func == "?":
        print_help()
    elif func == "exit":
        b_is_exit = True
    elif func == "메모장":
        add_memo()
    else:
        print("올바른 기능을 입력해 주세요.")
