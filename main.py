from datetime import datetime, timedelta

class Rental:
    def __init__(self, item, daily_rate, start_date, duration_days):
        self.item = item
        self.daily_rate = daily_rate
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.end_date = self.start_date + timedelta(days=duration_days)

    def total_cost(self):
        return self.daily_rate * self.duration_days

    def __repr__(self):
        return f"{self.item}: {self.daily_rate}원/일, {self.duration_days}일 대여, 반납일: {self.end_date.strftime('%Y-%m-%d')}"

def main():
    rentals = []

    while True:
        print("\n1. 장기 대여 추가")
        print("2. 장기 대여 목록 조회")
        print("3. 총 대여 비용 조회")
        print("4. 종료")

        choice = input("원하는 작업의 번호를 선택하세요: ")

        if choice == '1':
            item = input("대여 항목 이름: ")
            daily_rate = int(input("일일 대여 요금: "))
            start_date = input("대여 시작일 (YYYY-MM-DD): ")
            duration_days = int(input("대여 기간 (일): "))
            rentals.append(Rental(item, daily_rate, start_date, duration_days))
            print(f"장기 대여 항목 '{item}'가 추가되었습니다.")

        elif choice == '2':
            if not rentals:
                print("장기 대여 항목이 없습니다.")
            else:
                for rental in rentals:
                    print(rental)

        elif choice == '3':
            total_cost = sum(rental.total_cost() for rental in rentals)
            print(f"총 대여 비용: {total_cost}원")

        elif choice == '4':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
