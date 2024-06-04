from datetime import datetime, timedelta

class Saving:
    def __init__(self):
        self.savings_list = []  # 적금 목록을 저장할 리스트 초기화

    def add_savings(self):
        # 은행 이름 입력
        bank_name = input("은행 이름을 입력하세요: ")
        
        # 적금 금액 입력 및 유효성 검사
        while True:
            amount = input("적금 금액을 입력하세요: ")
            if amount.isdigit():
                amount = float(amount)
                break
            else:
                print("숫자만 입력하세요.")
        
        # 동일 은행 적금이 이미 있는 경우 금액 추가
        for savings in self.savings_list:
            if bank_name == savings["bank_name"]:
                savings["amount"] += amount
                print("적금이 추가되었습니다.")
                return
        
        # 적금 시작일 입력 및 유효성 검사
        while True:
            try:
                start_date = input("적금 시작일을 입력하세요 (YYYY-MM-DD): ")
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("날짜 형식이 올바르지 않습니다. 다시 입력해 주세요.")
        
        # 적금 만기일 입력 및 유효성 검사
        while True:
            try:
                end_date = input("적금 만기일을 입력하세요 (YYYY-MM-DD): ")
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                if end_date <= start_date:
                    raise ValueError("만기일은 시작일보다 늦어야 합니다.")
                break
            except ValueError as e:
                print(f"오류: {e} 다시 입력해 주세요.")
        
        # 적금 이율 입력 및 유효성 검사
        while True:
            try:
                interest = float(input("만기적금 이율을 입력하세요 (n%): ").replace('%', '')) / 100
                break
            except ValueError:
                print("올바른 이율을 입력해 주세요.")
        
        # 새로운 적금 항목 추가
        new_savings = {
            "bank_name": bank_name,
            "amount": amount,
            "start_date": start_date,
            "end_date": end_date,
            "interest": interest
        }
        self.savings_list.append(new_savings)
        print("적금이 추가되었습니다.")

    def view_savings(self):
        # 적금 목록이 비어 있는 경우 메시지 출력
        if not self.savings_list:
            print("등록된 적금이 없습니다.")
        else:
            print("적금 목록:")
            # 적금 목록 출력
            for idx, savings in enumerate(self.savings_list, start=1):
                # 남은 날짜 계산
                days_remaining = (savings['end_date'] - datetime.now().date()).days
                # 만기 시 환급 금액 계산
                maturity_amount = savings['amount'] * (1 + savings['interest'])
                print(f"{idx}. 은행: {savings['bank_name']}, 금액: {savings['amount']}, 시작일: {savings['start_date']}, 종료일: {savings['end_date']}")
                print(f"만기까지 남은 날짜: {days_remaining}일, 환급 금액: {maturity_amount:.2f}")

def main():
    save = Saving()
    while True:
        # 사용자 선택 메뉴
        print("1. 적금하기")
        print("2. 적금 목록보기")
        print("exit 입력시 종료")
        choice = input("적금 항목입니다 원하는 번호를 눌러 주십시오: ")
        if choice == "1":
            save.add_savings()
        elif choice == "2":
            save.view_savings()
        elif choice.lower() == "exit":
            print("종료합니다.")
            break
        else:
            print("올바른 기능을 입력해 주세요.")

if __name__ == "__main__":
    main()
