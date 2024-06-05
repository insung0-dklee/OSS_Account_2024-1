from datetime import datetime, timedelta

#기념일 관리 프로그램
#1. 기념일 추가
#2. 다가오는 기념일 보기
#3. 기념일 삭제
#4. 기념일 수정
#5. 기념일 목록 한번에 보기
#6. 종료
#원하는 작업을 선택하세요: 1
#기념일 이름을 입력하세요: 생일
#기념일 날짜를 입력하세요 (YYYY-MM-DD): 2024-06-15
#기념일 '생일'이(가) 2024-06-15에 추가되었습니다.

#원하는 작업을 선택하세요: 2
#며칠 후까지의 기념일을 보시겠습니까?: 30

#원하는 작업을 선택하세요: 3
#삭제할 기념일 이름을 입력하세요: 생일
#기념일 '생일'이(가) 삭제되었습니다.

#원하는 작업을 선택하세요: 4


#원하는 작업을 선택하세요: 5
#기념일 목록:
#결혼기념일 - 2024-06-15

#원하는 작업을 선택하세요: 6
#종료

class EventManager:
    def __init__(self):
        self.events = []  # 기념일을 저장할 리스트

    def add_event(self, name, date):#기념일을 정의하고 리스트에 추가함.
        event = {
            'name': name,
            'date': date
        }
        self.events.append(event)  # 기념일을 리스트에 추가
        print(f"기념일 '{name}'이(가) {date.strftime('%Y-%m-%d')}에 추가되었습니다.")

    def get_upcoming_events(self, days=30):#현재 날짜와 비교하여 기념일반환
        today = datetime.now().date()#현재날짜
        # 주어진 기간 내의 다가오는 기념일을 반환
        upcoming_events = [
            event for event in self.events
            if today <= event['date'] <= today + timedelta(days=days)
        ]
        return upcoming_events

    def delete_event(self, name):
        initial_count = len(self.events)
        self.events = [event for event in self.events if event['name'] != name]
        if len(self.events) < initial_count:
            print(f"기념일 '{name}'이(가) 삭제되었습니다.")
        else:
            print(f"기념일 '{name}'을(를) 찾을 수 없습니다. 잘못 입력하셨습니다.")

    def edit_event(self, old_name, new_name, new_date):
        for event in self.events:
            if event['name'] == old_name:
                event['name'] = new_name
                event['date'] = new_date
                print(f"기념일 '{old_name}'이(가) '{new_name}'으로 {new_date.strftime('%Y-%m-%d')}에 수정되었습니다.")
                return
        print(f"기념일 '{old_name}'을(를) 찾을 수 없습니다.")

    def list_all_events(self):
        if not self.events:
            print("등록된 기념일이 없습니다.")
            return
        print("\n기념일 목록:")
        for event in self.events:
            print(f"{event['name']} - {event['date']}")

def main():
    manager = EventManager()

    while True:
        print("\n기념일 관리 프로그램")
        print("1. 기념일 추가")
        print("2. 다가오는 기념일 보기")
        print("3. 기념일 삭제")
        print("4. 기념일 수정")
        print("5. 기념일 목록 한번에 보기")
        print("6. 종료")
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
            name = input("삭제할 기념일 이름을 입력하세요: ")
            manager.delete_event(name)
        elif choice == '4':
            old_name = input("수정할 기념일 이름을 입력하세요: ")
            new_name = input("새 기념일 이름을 입력하세요: ")
            date_str = input("새 기념일 날짜를 입력하세요 (YYYY-MM-DD): ")
            try:
                new_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                manager.edit_event(old_name, new_name, new_date)
            except ValueError:
                print("날짜 입력이 올바르지 않습니다. 다시 시도하세요.")

        elif choice == '5':
            manager.list_all_events()

        elif choice == '6':
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()