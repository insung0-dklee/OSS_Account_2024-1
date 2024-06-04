class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number

class AccountRegistry:
    def __init__(self):
        self.accounts = {}
        self.account_numbers = set()

    def add_account(self, name, account_number):
        if not name or not account_number:
            print("이름과 계좌번호는 빈 값이 될 수 없습니다.")
            return
        if name in self.accounts:
            print(f"이미 등록된 이름입니다: {name}")
            return
        if account_number in self.account_numbers:
            print(f"이미 등록된 계좌번호입니다: {account_number}")
            return
        self.accounts[name] = Account(name, account_number)
        self.account_numbers.add(account_number)
        print(f"{name}의 계좌 ({account_number})가 등록되었습니다.")

    def find_account(self, name):
        return self.accounts.get(name, None)

def main():
    registry = AccountRegistry()

    # 친구 등록
    while True:
        name = input("저장하고 싶은 계좌주의 이름을 입력하세요 (종료하려면 '종료' 입력): ")
        if name == "종료":
            break
        account_number = input(f"{name}의 계좌번호를 입력하세요: ")
        registry.add_account(name, account_number)

    # 계좌 찾기
    while True:
        search_name = input("찾고 싶은 계좌주의 이름을 입력하세요 (종료하려면 '종료' 입력): ")
        if search_name == "종료":
            break
        account = registry.find_account(search_name)
        if account:
            print(f"{account.name}의 계좌번호: {account.account_number}")
        else:
            print("해당하는 계좌를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
