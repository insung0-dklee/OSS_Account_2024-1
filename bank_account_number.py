class Account:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
"""
계좌등록 클래스입니다.
name: 이름,
account_number: 계좌번호
add_account: 이름과 계좌번호를 조회해서 중복의 유무를 조회하고,
중복이 되지않으면 이름으로 딕셔너리를 만들어서 이름과 계좌번호를 추가하고 등록되었다고 출력합니다.
find_account: 이름을 통해서 accounts에서 가지고 옵니다.
"""
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