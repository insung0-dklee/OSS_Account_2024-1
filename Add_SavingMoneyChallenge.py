import datetime

# 저축 챌린지를 관리하는 클래스 정의
class SavingsChallenge:
    def __init__(self, daily_amount, days):
        self.daily_amount = daily_amount  # 매일 저축할 금액
        self.days = days  # 챌린지 기간 (일 수)
        self.start_date = datetime.date.today()  # 챌린지를 시작하는 날짜
        self.total_saved = 0  # 현재까지 저축된 총 금액

    # 매일 저축하는 메서드
    def save_daily(self):
        for day in range(1, self.days + 1):
            self.total_saved += self.daily_amount  # 매일 저축할 금액을 총 저축 금액에 더함
            current_date = self.start_date + datetime.timedelta(days=day - 1)  # 현재 날짜 계산
            print(f"Day {day}: Saved {self.daily_amount} units. Total saved: {self.total_saved} units. Date: {current_date}")

    # 총 저축 금액을 반환하는 메서드
    def get_total_savings(self):
        return self.total_saved

if __name__ == "__main__":
    # 사용자로부터 매일 저축할 금액과 챌린지 기간을 입력받음
    daily_amount = int(input("Enter the daily saving amount: "))
    days = int(input("Enter the number of days for the challenge: "))

    # SavingsChallenge 객체 생성 및 저축 챌린지 시작
    challenge = SavingsChallenge(daily_amount, days)
    challenge.save_daily()

    # 챌린지 완료 후 총 저축 금액 출력
    print(f"Challenge completed! Total savings: {challenge.get_total_savings()} units.")