import json
from datetime import datetime

class AutoSave:
    def __init__(self, username, save_amount):
        self.username = username
        self.save_amount = save_amount
        self.auto_save_data = f"{username}_autosave.json"
        self.savings = 0
        self.load_savings()

    def load_savings(self):
        try:
            with open(self.auto_save_data, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.savings = data.get("savings", 0)
        except FileNotFoundError:
            self.savings = 0

    def save_savings(self):
        with open(self.auto_save_data, 'w', encoding='utf-8') as file:
            json.dump({"savings": self.savings}, file, ensure_ascii=False, indent=4)

    def add_savings(self):
        self.savings += self.save_amount
        self.save_savings()
        print(f"자동으로 {self.save_amount}원이 저축되었습니다. 현재 저축액: {self.savings}원")

    def view_savings(self):
        print(f"현재까지 저축된 금액은 {self.savings}원입니다.")

def setup_auto_save():
    username = input("사용자 이름을 입력하세요: ")
    save_amount = float(input("매월 자동으로 저축할 금액을 입력하세요: "))
    auto_save = AutoSave(username, save_amount)
    return auto_save

def auto_save_menu():
    auto_save = None
    while True:
        print("\n--- 자동 절약 기능 ---")
        print("1: 자동 저축 설정")
        print("2: 자동 저축 실행")
        print("3: 현재 저축액 확인")
        print("0: 메인 메뉴로 돌아가기")
        choice = input("기능을 선택하세요: ")

        if choice == "1":
            auto_save = setup_auto_save()
        elif choice == "2":
            if auto_save:
                auto_save.add_savings()
            else:
                print("자동 저축 설정을 먼저 해주세요.")
        elif choice == "3":
            if auto_save:
                auto_save.view_savings()
            else:
                print("자동 저축 설정을 먼저 해주세요.")
        elif choice == "0":
            break
        else:
            print("올바른 기능을 선택하세요.")
