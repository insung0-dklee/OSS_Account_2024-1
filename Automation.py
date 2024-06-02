import json
from datetime import datetime, timedelta

# 자동화 규칙을 저장할 파일
automation_file = 'automation_rules.json'

# 초기 자동화 규칙을 저장할 함수
def save_automation_rules(rules):
    with open(automation_file, 'w') as file:
        json.dump(rules, file, ensure_ascii=False, indent=4)

# 자동화 규칙을 불러올 함수
def load_automation_rules():
    try:
        with open(automation_file, 'r') as file:
            rules = json.load(file)
        return rules
    except FileNotFoundError:
        return []

# 자동화 규칙을 추가하는 함수
def add_automation_rule():
    rule = {}
    rule['type'] = input("자동화할 항목의 유형을 입력하세요 (수입/지출): ")
    rule['amount'] = float(input("금액을 입력하세요: "))
    rule['description'] = input("설명을 입력하세요: ")
    rule['interval'] = input("반복 주기를 입력하세요 (daily/weekly/monthly): ")
    rule['start_date'] = input("시작 날짜를 입력하세요 (YYYY-MM-DD): ")
    rule['last_executed'] = None

    rules = load_automation_rules()
    rules.append(rule)
    save_automation_rules(rules)
    print("자동화 규칙이 추가되었습니다.")

# 자동화 규칙을 실행하는 함수
def execute_automation_rules(ledger):
    rules = load_automation_rules()
    today = datetime.now().date()
    
    for rule in rules:
        start_date = datetime.strptime(rule['start_date'], "%Y-%m-%d").date()
        last_executed = datetime.strptime(rule['last_executed'], "%Y-%m-%d").date() if rule['last_executed'] else None
        interval = rule['interval']
        
        should_execute = False
        
        if interval == 'daily':
            should_execute = not last_executed or (today - last_executed).days >= 1
        elif interval == 'weekly':
            should_execute = not last_executed or (today - last_executed).days >= 7
        elif interval == 'monthly':
            should_execute = not last_executed or (today - last_executed).days >= 30
        
        if should_execute and today >= start_date:
            if rule['type'] == '수입':
                day_income(ledger, rule['amount'], rule['description'])
            elif rule['type'] == '지출':
                day_spending(ledger, rule['amount'], rule['description'])
            rule['last_executed'] = today.strftime("%Y-%m-%d")
    
    save_automation_rules(rules)
    print("자동화 규칙이 실행되었습니다.")

# 자동화 규칙을 조회하는 함수
def view_automation_rules():
    rules = load_automation_rules()
    if not rules:
        print("등록된 자동화 규칙이 없습니다.")
    else:
        for idx, rule in enumerate(rules, start=1):
            print(f"{idx}. 유형: {rule['type']}, 금액: {rule['amount']}, 설명: {rule['description']}, 주기: {rule['interval']}, 시작 날짜: {rule['start_date']}, 마지막 실행: {rule['last_executed']}")
