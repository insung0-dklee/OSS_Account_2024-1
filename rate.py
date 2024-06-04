# 자신의 소비에 대한 평가
#기능추가,자신의 일주일 소비에 대한 만족도 기록 

"""
사용자가 매주 자신의 소비에 대한 만족도를 1-5로 입력하여 자신의 소비에 대해서 쉽게 되돌아 볼 수 있게 구현 하였습니다.
입력한 날짜와 만족도가 파일에 저장될 수 있게 하였습니다.
또한, 다음 기록 일정도 알려줍니다.
"""
import os
from datetime import datetime, timedelta

# 파일 이름 설정
file_name = "consumption_satisfaction.txt"

# 파일이 없으면 생성
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        file.write("Date,Satisfaction\n")
# 사용자 입력 함수
def get_user_satisfaction():
    while True:
        try:
            satisfaction = int(input("이번 주 소비에 대한 만족도를 1에서 5 사이로 입력하세요: "))
            if 1 <= satisfaction <= 5:
                return satisfaction
            else:
                print("1에서 5 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")
            
#파일에 만족도를 기록하는 함수 
def record_satisfaction(satisfaction):
    with open(file_name, 'a') as file:
        date_str = datetime.now().strftime("%Y-%m-%d")
        file.write(f"{date_str},{satisfaction}\n")
#마지막 기록 날짜 확인 함수 
def check_last_entry_date():
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) > 1:
                last_entry = lines[-1]
                last_date_str = last_entry.split(',')[0]
                last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
                return last_date
            else:
                return None
    except FileNotFoundError:
        return None
#메인
def main():
    last_date = check_last_entry_date()
    today = datetime.now()

    if last_date:
        days_since_last_entry = (today - last_date).days
        #일주일이 지나기전에 다시열면 기록을 못 하게하여, 일주일 간격으로 작성하는것을 원칙으로 함 
        if days_since_last_entry < 7:
            print(f"마지막 기록이 {days_since_last_entry}일 전입니다. 다음 기록은 {7 - days_since_last_entry}일 후에 가능합니다.")
            return

    satisfaction = get_user_satisfaction()
    record_satisfaction(satisfaction)
    print("만족도가 성공적으로 기록되었습니다.")

if __name__ == "__main__":
    main()