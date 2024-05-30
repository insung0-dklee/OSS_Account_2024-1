import hashlib #hashlib 사용
import json
import os

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
    