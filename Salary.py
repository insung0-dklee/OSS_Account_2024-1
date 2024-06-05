import datetime

class PartTimeEmployee:
    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage
        self.daily_hours = {}

    def add_work_hours(self, date, hours_worked):
        if date in self.daily_hours:
            overwrite = input(f"{date}의 근무 시간은 이미 등록되어 있습니다. 수정하시겠습니까? (y/n): ")
            if overwrite.lower() == 'y':
                self.daily_hours[date] = hours_worked
                print(f"{date}의 근무 시간이 업데이트되었습니다.")
        else:
            self.daily_hours[date] = hours_worked
            print(f"{date}의 근무 시간이 정상적으로 추가되었습니다.")

    def calculate_monthly_salary(self, year, month):
        total_hours = sum(hours for date, hours in self.daily_hours.items() if date.year == year and date.month == month)
        return self.hourly_wage * total_hours

def main():
    employees = {}

    while True:
        print("\n1. 알바생 정보 추가")
        print("2. 근무 시간 추가")
        print("3. 월급 계산")
        print("4. 알바생 정보 삭제")
        print("5. 근무 시간 조회")
        print("6. 알바생 목록 출력")
        print("7. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            name = input("알바생 이름을 입력하세요: ")
            hourly_wage = float(input("시급을 입력하세요: "))
            employees[name] = PartTimeEmployee(name, hourly_wage)
            print(f"{name}님의 정보가 추가되었습니다.")
        elif choice == '2':
            name = input("알바생 이름을 입력하세요: ")
            if name in employees:
                date_input = input("근무한 날짜를 입력하세요 (예: 2000-10-10): ")
                date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                hours_worked = float(input("근무 시간을 입력하세요: "))
                employees[name].add_work_hours(date, hours_worked)
            else:
                print("등록된 알바생이 아닙니다. 먼저 알바생 정보를 추가하세요.")
        elif choice == '3':
            name = input("알바생 이름을 입력하세요: ")
            if name in employees:
                date_input = input("월급을 계산할 년도와 달을 입력하세요. (예: 2020-05): ")
                year, month = map(int, date_input.split('-'))
                salary = employees[name].calculate_monthly_salary(year, month)
                print(f"{name}님의 {year}년 {month}월 월급은 {salary:.2f}원 입니다.")
            else:
                print("등록된 알바생이 아닙니다. 먼저 알바생 정보를 추가하세요.")
        elif choice == '4':
            name = input("삭제할 알바생 이름을 입력하세요: ")
            if name in employees:
                del employees[name]
                print(f"{name}님의 정보가 삭제되었습니다.")
            else:
                print("등록된 알바생이 아닙니다.")

        elif choice == '5':
            name = input("알바생 이름을 입력하세요: ")
            if name in employees:
                try:
                    start_date_input = input("조회 시작 날짜를 입력하세요 (예: 2000-10-10): ")
                    start_date = datetime.datetime.strptime(start_date_input, '%Y-%m-%d').date()
                    end_date_input = input("조회 종료 날짜를 입력하세요 (예: 2000-10-20): ")
                    end_date = datetime.datetime.strptime(end_date_input, '%Y-%m-%d').date()
                    if start_date > end_date:
                        print("시작 날짜가 종료 날짜보다 클 수 없습니다.")
                    else:
                        print(f"\n{name}님의 근무 시간 조회 ({start_date} ~ {end_date}):")
                        for date, hours in employees[name].daily_hours.items():
                            if start_date <= date <= end_date:
                                print(f"{date}: {hours}시간")
                except ValueError:
                    print("날짜 형식이 올바르지 않습니다.")
            else:
                print("등록된 알바생이 아닙니다.")
                
        elif choice == '6':
            if employees:
                print("\n현재 등록된 알바생 목록:")
                for name in employees:
                    print(f"- {name}")
            else:
                print("등록된 알바생이 없습니다.")
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()