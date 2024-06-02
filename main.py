import json
from datetime import datetime

class BudgetManager:
    def __init__(self):
        self.balance = 0  # 잔액 초기화
        self.transactions = []  # 트랜잭션 목록 초기화
        self.goals = {}  # 목표 목록 초기화
        self.points = 0  # 포인트 초기화
        self.level = 1  # 레벨 초기화
        self.badges = []  # 배지 목록 초기화
    
    def add_transaction(self, amount, category):
        """ 트랜잭션 추가 메서드 """
        self.transactions.append({'amount': amount, 'category': category, 'date': str(datetime.now())})
        # 트랜잭션을 목록에 추가
        self.balance += amount  # 잔액 업데이트
        self._update_goals(amount)  # 목표 업데이트
        self._check_goals()  # 목표 달성 여부 체크
        self._add_points(amount)  # 포인트 적립
    
    def set_goal(self, name, target_amount):
        """ 목표 설정 메서드 """
        self.goals[name] = {'target_amount': target_amount, 'current_amount': 0}
        # 목표를 목록에 추가
    
    def _update_goals(self, amount):
        """ 트랜잭션에 따라 목표 업데이트 """
        for goal in self.goals.values():
            if amount < 0:
                goal['current_amount'] += abs(amount)  # 지출은 목표 달성에 기여하지 않음
            else:
                goal['current_amount'] += amount  # 수입은 목표 달성에 기여
    
    def _check_goals(self):
        """ 목표 달성 여부를 확인하고, 달성 시 보상 제공 """
        for goal_name, goal in self.goals.items():
            if goal['current_amount'] >= goal['target_amount']:
                print(f"Goal '{goal_name}' achieved!")  # 목표 달성 메시지 출력
                self.points += 100  # 목표 달성 보상으로 포인트 제공
                self.award_badge(f"Goal '{goal_name}' Achieved")  # 목표 달성 배지 수여
                self._level_up()  # 레벨 업 체크
    
    def _add_points(self, amount):
        """ 지출액에 따른 포인트 적립 """
        if amount < 0:
            self.points += abs(amount) // 10  # 지출액의 10%를 포인트로 적립
    
    def _level_up(self):
        """ 포인트에 따라 레벨 업 """
        if self.points >= self.level * 100:
            self.level += 1
            print(f"Congratulations! You've reached level {self.level}.")  # 레벨 업 메시지 출력
    
    def award_badge(self, badge_name):
        """ 배지 제공 메서드 """
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            print(f"Badge '{badge_name}' awarded!")  # 배지 수여 메시지 출력
    
    def save_data(self, filename):
        """ 데이터를 파일에 저장 """
        data = {
            'balance': self.balance,
            'transactions': self.transactions,
            'goals': self.goals,
            'points': self.points,
            'level': self.level,
            'badges': self.badges
        }
        with open(filename, 'w') as f:
            json.dump(data, f)  # 데이터를 JSON 형식으로 저장
    
    def load_data(self, filename):
        """ 파일에서 데이터 불러오기 """
        with open(filename, 'r') as f:
            data = json.load(f)
            self.balance = data['balance']
            self.transactions = data['transactions']
            self.goals = data['goals']
            self.points = data['points']
            self.level = data['level']
            self.badges = data['badges']

# 사용 예시
manager = BudgetManager()
manager.set_goal('Vacation', 1000)  # 휴가를 위한 저축 목표 설정
manager.add_transaction(-50, 'Groceries')  # 식료품비 지출 추가
manager.add_transaction(200, 'Salary')  # 월급 수입 추가
manager.award_badge('First Transaction')  # 첫 트랜잭션 배지 수여
manager.save_data('budget_data.json')  # 데이터를 파일에 저장
