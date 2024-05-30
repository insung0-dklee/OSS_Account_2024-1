class HouseholdAccountBook:
    def __init__(self):
        self.records = []
        self.balance = 0
    
    def show_balance(self):
        print(f"현재 잔액: {self.balance}")


def main():
    book = HouseholdAccountBook()
    b_is_exit = 0

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
          pass
        elif func == "2":
          pass
        elif func == "3":
          pass
        elif func == "4":
            book.show_balance()

        elif func == "?":
            print("4: 현재 잔액 조회")
            print("5: 종료")

        elif func == "5":
            print("프로그램을 종료합니다.")
            b_is_exit = 1

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()