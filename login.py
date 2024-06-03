class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.logged_in_user = None
        self.sub_account_logged_in = None

    def create_account(self, username, password):
        if self.accounts:
            print("이미 본계정이 존재합니다. 본계정은 하나만 생성할 수 있습니다.")
        else:
            self.accounts[username] = {'password': password, 'sub_accounts': {}}
            print(f"계정이 생성되었습니다: {username}")

    def login(self, username, password):
        if username in self.accounts and self.accounts[username]['password'] == password:
            self.logged_in_user = username
            print(f"{username}님, 본계정으로 로그인 성공!")
        elif self.logged_in_user and username in self.accounts[self.logged_in_user]['sub_accounts'] and self.accounts[self.logged_in_user]['sub_accounts'][username] == password:
            self.sub_account_logged_in = username
            print(f"{username}님, 부계정으로 로그인 성공! 부계정으로 이용하시겠습니까? (y/n)")
            choice = input()
            if choice.lower() == 'y':
                self.logged_in_user = None
                print(f"{username}님, 부계정으로 전환되었습니다.")
            else:
                self.sub_account_logged_in = None
                print("부계정 로그인이 취소되었습니다.")
        else:
            print("로그인 실패! 사용자명 또는 비밀번호가 올바른지 확인하세요.")

    def logout(self):
        if self.logged_in_user:
            print(f"{self.logged_in_user}님, 로그아웃 되었습니다.")
            self.logged_in_user = None
        elif self.sub_account_logged_in:
            print(f"{self.sub_account_logged_in}님, 부계정에서 로그아웃 되었습니다.")
            self.sub_account_logged_in = None
        else:
            print("로그인된 사용자가 없습니다.")

    def add_sub_account(self, sub_username, sub_password):
        if self.logged_in_user and not self.sub_account_logged_in:
            sub_accounts = self.accounts[self.logged_in_user]['sub_accounts']
            if sub_username in sub_accounts:
                print("이미 존재하는 부계정 사용자명입니다.")
            else:
                sub_accounts[sub_username] = sub_password
                print(f"부계정이 추가되었습니다: {sub_username}")
        else:
            print("부계정을 추가하려면 먼저 본계정으로 로그인하세요.")

    def display_accounts(self):
        if self.logged_in_user:
            print(f"\n{self.logged_in_user}님의 부계정 목록:")
            sub_accounts = self.accounts[self.logged_in_user]['sub_accounts']
            if sub_accounts:
                for sub_username in sub_accounts:
                    print(f"부계정: {sub_username}")
            else:
                print("등록된 부계정이 없습니다.")
        else:
            print("본 계정으로 로그인 후 이용해주세요.")

def main():
    manager = AccountManager()

    while True:
        print("\n1. 계정 생성")
        print("2. 로그인")
        print("3. 로그아웃")
        print("4. 부계정 추가")
        print("5. 부계정 목록 표시")
        print("6. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            username = input("사용자명을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            manager.create_account(username, password)
        elif choice == '2':
            username = input("사용자명을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            manager.login(username, password)
        elif choice == '3':
            manager.logout()
        elif choice == '4':
            sub_username = input("추가할 부계정 사용자명을 입력하세요: ")
            sub_password = input(f"{sub_username}의 비밀번호를 입력하세요: ")
            manager.add_sub_account(sub_username, sub_password)
        elif choice == '5':
            manager.display_accounts()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
