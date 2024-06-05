from datetime import datetime, timedelta
import json

class Subscription:
    def __init__(self, name, monthly_cost, next_payment_date):
        """
        구독 서비스 초기화 함수
        name: 구독 서비스 이름
        monthly_cost: 월 비용
        next_payment_date: 다음 결제일 (YYYY-MM-DD 형식)
        """
        self.name = name
        self.monthly_cost = monthly_cost
        self.next_payment_date = datetime.strptime(next_payment_date, '%Y-%m-%d')

    def update_next_payment_date(self):
        """
        다음 결제일을 한 달 뒤로 설정하는 함수
        """
        self.next_payment_date += timedelta(days=30)

    def __str__(self):
        """
        구독 서비스 정보를 문자열로 반환하는 함수
        """
        return f"구독 서비스(이름: {self.name}, 월 비용: {self.monthly_cost}원, 다음 결제일: {self.next_payment_date.strftime('%Y-%m-%d')})"

class SubscriptionManager:
    def __init__(self):
        """
        구독 서비스 관리 클래스 초기화 함수
        """
        self.subscriptions = []

    def add_subscription(self, name, monthly_cost, next_payment_date):
        """
        구독 서비스를 추가하는 함수
        name: 구독 서비스 이름
        monthly_cost: 월 비용
        next_payment_date: 다음 결제일 (YYYY-MM-DD 형식)
        """
        subscription = Subscription(name, monthly_cost, next_payment_date)
        self.subscriptions.append(subscription)
        print(f"구독 서비스 '{name}'가 추가되었습니다.")

    def remove_subscription(self, name):
        """
        구독 서비스를 삭제하는 함수
        name: 구독 서비스 이름
        """
        self.subscriptions = [s for s in self.subscriptions if s.name != name]
        print(f"구독 서비스 '{name}'가 삭제되었습니다.")

    def view_subscriptions(self):
        """
        모든 구독 서비스를 출력하는 함수
        """
        if not self.subscriptions:
            print("등록된 구독 서비스가 없습니다.")
        for subscription in self.subscriptions:
            print(subscription)

    def check_payments_due(self):
        """
        결제일이 도래한 구독 서비스를 확인하는 함수
        """
        today = datetime.today()
        for subscription in self.subscriptions:
            if subscription.next_payment_date <= today:
                print(f"'{subscription.name}'의 결제일이 도래했습니다.")
                subscription.update_next_payment_date()

    def save_subscriptions(self, filename):
        """
        구독 서비스 정보를 파일에 저장하는 함수
        filename: 저장할 파일 이름
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([s.__dict__ for s in self.subscriptions], file, default=str, ensure_ascii=False, indent=4)
        print("구독 서비스 정보가 파일에 저장되었습니다.")

    def load_subscriptions(self, filename):
        """
        파일에서 구독 서비스 정보를 불러오는 함수
        filename: 불러올 파일 이름
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                subscriptions_data = json.load(file)
                self.subscriptions = [
                    Subscription(s['name'], s['monthly_cost'], s['next_payment_date'])
                    for s in subscriptions_data
                ]
            print("파일에서 구독 서비스 정보를 불러왔습니다.")
        except FileNotFoundError:
            print("저장된 구독 서비스 정보를 찾을 수 없습니다.")


def main():
    """
    구독 서비스 관리 메인 함수
    """
    manager = SubscriptionManager()

    while True:
        print("\n1: 구독 서비스 추가")
        print("2: 구독 서비스 삭제")
        print("3: 구독 서비스 보기")
        print("4: 결제일 도래 확인")
        print("5: 구독 서비스 저장")
        print("6: 구독 서비스 불러오기")
        print("0: 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("구독 서비스 이름을 입력하세요: ")
            monthly_cost = float(input("월 비용을 입력하세요: "))
            next_payment_date = input("다음 결제일을 입력하세요 (YYYY-MM-DD): ")
            manager.add_subscription(name, monthly_cost, next_payment_date)
        elif choice == '2':
            name = input("삭제할 구독 서비스 이름을 입력하세요: ")
            manager.remove_subscription(name)
        elif choice == '3':
            manager.view_subscriptions()
        elif choice == '4':
            manager.check_payments_due()
        elif choice == '5':
            filename = input("구독 서비스 정보를 저장할 파일명을 입력하세요: ")
            manager.save_subscriptions(filename)
        elif choice == '6':
            filename = input("구독 서비스 정보를 불러올 파일명을 입력하세요: ")
            manager.load_subscriptions(filename)
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")