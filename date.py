from datetime import datetime, timedelta

class EventManager:
    def __init__(self):
        self.events = []  # 기념일을 저장할 리스트

    def add_event(self, name, date):
        event = {
            'name': name,
            'date': date
        }
        self.events.append(event)  # 기념일을 리스트에 추가
        print(f"기념일 '{name}'이(가) {date.strftime('%Y-%m-%d')}에 추가되었습니다.")

    def get_upcoming_events(self, days=30):
        today = datetime.now().date()
        # 주어진 기간 내의 다가오는 기념일을 반환
        upcoming_events = [
            event for event in self.events
            if today <= event['date'] <= today + timedelta(days=days)
        ]
        return upcoming_events

def main():
    manager = EventManager()

    while True:
        print("\n기념일 관리 프로그램")
        print("1. 기념일 추가")
        print("2. 다가오는 기념일 보기")
        print("3. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("기념일 이름을 입력하세요: ")
            date_str = input("기념일 날짜를 입력하세요 (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                manager.add_event(name, date)
            except ValueError:
                print("날짜 입력이 올바르지 않습니다. 다시 시도하세요.")
        elif choice == '2':
            days = int(input("며칠 후까지의 기념일을 보시겠습니까?: "))
            upcoming_events = manager.get_upcoming_events(days)
            if upcoming_events:
                print("\n다가오는 기념일:")
                for event in upcoming_events:
                    print(f"{event['name']} - {event['date']}")
            else:
                print("다가오는 기념일이 없습니다.")
        elif choice == '3':
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
