# 가계부 프로그램
# 1번에 소비분야와 지출금액을 저장하는 기능 구현

class HouseholdAccountBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, category, amount):
        self.entries.append({'category': category, 'amount': amount})

    def show_entries(self):
        if not self.entries:
            print("입력된 내역이 없습니다.")
        else:
            print("가계부 내역:")
            total = 0
            for entry in self.entries:
                print(f"분야: {entry['category']}, 금액: {entry['amount']}원")
                total += entry['amount']
            print(f"총 지출: {total}원")

def run_account_book():
    account_book = HouseholdAccountBook()
    categories = ["식비", "교통비", "생활비", "의료비", "교육비", "기타"]

    while True:
        print("\n소비분야를 선택하세요:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        print("0. 종료")

        try:
            choice = int(input("선택: "))
            if choice == 0:
                break
            elif 1 <= choice <= len(categories):
                category = categories[choice - 1]
                amount = int(input(f"{category} 금액을 입력하세요: "))
                account_book.add_entry(category, amount)
            else:
                print("잘못된 선택입니다. 다시 선택하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    account_book.show_entries()

def main():
    b_is_exit = False

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
            run_account_book()
        elif func == "2":
            print("기능 2가 아직 구현되지 않았습니다.")
        elif func == "3":
            print("기능 3가 아직 구현되지 않았습니다.")
        elif func == "?":
            print("도움말: \n1. 가계부 입력\n2. 기능 2\n3. 기능 3\n0. 종료")
        elif func == "0":
            b_is_exit = True
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
