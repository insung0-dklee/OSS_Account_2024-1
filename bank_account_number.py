import random
from datetime import datetime
class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.registration_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class AccountRegistry:
    def __init__(self):
        self.accounts = {}
    def add_account(self, name, account_number):
        if name in self.accounts:
            print(f"이미 등록된 이름입니다: {name}")
            return
        if account_number in [account.account_number for account in self.accounts.values()]:
            print(f"이미 등록된 계좌번호입니다: {account_number}")
            return
        self.accounts[name] = Account(name, account_number)
        print(f"{name}의 계좌 ({account_number})가 등록되었습니다. 등록 시간: {self.accounts[name].registration_time}")

    def find_account(self, name):
        return self.accounts.get(name, None)

    def edit_account(self, name):
        account = self.find_account(name)
        if not account:
            print("해당하는 계좌를 찾을 수 없습니다.")
            return
        new_name = input(f"새로운 이름을 입력하세요 (현재 이름: {account.name}): ") or account.name
        new_account_number = input(f"새로운 계좌번호를 입력하세요 (현재 계좌번호: {account.account_number}): ") or account.account_number
        self.accounts.pop(account.name)
        self.accounts[new_name] = Account(new_name, new_account_number)
        self.accounts[new_name].registration_time = account.registration_time
        print("계좌 정보가 수정되었습니다.")

    def delete_account(self, name):
        account = self.find_account(name)
        if not account:
            print("해당하는 계좌를 찾을 수 없습니다.")
            return
        self.accounts.pop(account.name)
        print(f"{name}의 계좌가 삭제되었습니다.")

    def list_accounts(self):
        if not self.accounts:
            print("등록된 계좌가 없습니다.")
            return
        print("\n등록된 계좌 목록:")
        for name, account in self.accounts.items():
            print(f"{name} - {account.account_number} (등록 시간: {account.registration_time})")



def generate_random_name():
    first_names = ['김', '이', '박', '최', '정']
    last_names = ['철수', '영희', '민수', '수지', '지훈']
    return random.choice(first_names) + random.choice(last_names)

def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == '예' or answer == '아니오':
            return answer
        print("잘못된 입력입니다. '예' 또는 '아니오'를 입력하세요.")



def main():
    registry = AccountRegistry()

    while True:
        print("\n계좌 관리 프로그램")
        print("1. 계좌 등록")
        print("2. 계좌 검색")
        print("3. 계좌 목록 보기")
        print("4. 계좌 수정")
        print("5. 계좌 삭제")
        print("6. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            use_random_name = get_yes_or_no("랜덤 이름을 사용하시겠습니까? (예/아니오): ")
            if use_random_name == '예':
                name = generate_random_name()
                print(f"추천된 이름: {name}")
            else:
                name = input("저장하고 싶은 계좌주의 이름을 입력하세요: ")

            account_number = input(f"{name}의 계좌번호를 입력하세요: ")
            registry.add_account(name, account_number)

        elif choice == '2':
            search_name = input("찾고 싶은 계좌주의 이름을 입력하세요: ")
            account = registry.find_account(search_name)
            if account:
                print(f"{account.name}의 계좌번호: {account.account_number} - 등록 시간: {account.timestamp}")
            else:
                print("해당하는 계좌를 찾을 수 없습니다.")

        elif choice == '3':
            registry.list_accounts()

        elif choice == '4':
            name = input("수정할 계좌주의 이름을 입력하세요: ")
            registry.edit_account(name)

        elif choice == '5':
            name = input("삭제할 계좌주의 이름을 입력하세요: ")
            registry.delete_account(name)

        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()