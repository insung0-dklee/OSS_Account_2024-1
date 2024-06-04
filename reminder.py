import json
from datetime import datetime, timedelta

reminder_file = 'reminders.json'

def load_reminders():
    try:
        with open(reminder_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_reminders(reminders):
    with open(reminder_file, 'w', encoding='utf-8') as file:
        json.dump(reminders, file, ensure_ascii=False, indent=4)

def add_reminder():
    message = input("리마인더 메시지: ")
    reminder_date = input("리마인더 날짜 (YYYY-MM-DD): ")
    reminder_time = input("리마인더 시간 (HH:MM): ")

    reminder = {
        "message": message,
        "date": reminder_date,
        "time": reminder_time
    }

    reminders = load_reminders()
    reminders.append(reminder)
    save_reminders(reminders)
    print("리마인더가 추가되었습니다.")

def view_reminders():
    reminders = load_reminders()
    if reminders:
        print("현재 리마인더 목록:")
        for idx, reminder in enumerate(reminders, start=1):
            print(f"{idx}. {reminder['date']} {reminder['time']} - {reminder['message']}")
    else:
        print("등록된 리마인더가 없습니다.")

def delete_reminder():
    view_reminders()
    reminders = load_reminders()
    if reminders:
        reminder_idx = int(input("삭제할 리마인더 번호를 입력하세요: ")) - 1
        if 0 <= reminder_idx < len(reminders):
            deleted = reminders.pop(reminder_idx)
            save_reminders(reminders)
            print(f"리마인더 '{deleted['message']}'가 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    else:
        print("삭제할 리마인더가 없습니다.")

def check_reminders():
    reminders = load_reminders()
    current_time = datetime.now()
    for reminder in reminders:
        reminder_time = datetime.strptime(f"{reminder['date']} {reminder['time']}", '%Y-%m-%d %H:%M')
        if current_time >= reminder_time:
            print(f"리마인더 알림: {reminder['message']}")
            reminders.remove(reminder)
    save_reminders(reminders)
