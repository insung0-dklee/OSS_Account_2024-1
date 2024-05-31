from datetime import datetime

class Account_book: # 가계부 클래스

  bal = 0 #잔액 - 미설정시 0원
  income_total = 0 #수입 총액
  income_list = [] #수입 기록 리스트
  spend_total = 0 #지출 총액
  spend_list = [] #지출 기록 리스트
  name = " " #이름 - 미설정시 공백

  fixed_list=[] #고정 지출 리스트

  def __init__(self,name,bal): # 초기화
    self.name = name #이름 설정
    if(bal>0):  #잔액 설정
      self.income_total += bal
      self.bal = bal
    else: #잔액이 0원보다 낮으면 0원으로 설정
      print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

  def income(self):# 수입 입력시 추가
    income_money = int(input("수입을 입력하세요 "))
    if(income_money < 0):#수입 잘못 입력 방지
      print("0 미만의 값을 입력하셨습니다.")
      return 0
    self.bal += income_money #금액 추가 및 내역을 리스트에 넣기
    self.income_list.append (income_money)
    self.income_total += income_money

  def spend(self):#지출 입력시 추가
    spend_money = int(input("지출을 입력하세요 "))
    if(spend_money < 0 or spend_money > self.bal):#지출 잘못 입력 방지
      print("값을 잘못 입력하셨습니다.")
      return 0
    self.bal -= spend_money #금액 감소 및 내역을 리스트에 넣기
    self.spend_list.append(spend_money)
    self.spend_total += spend_money

  def show_account(self): #금액 출력
    print("현재 남은 금액은: ",self.bal, "원 입니다.")

  def show_total(self): #수입,지출 총액 출력
    print("현재까지 소득의 총합은 ",self.income_total,"원 입니다.")
    print("현재까지 지출의 총합은 ",self.spend_total,"원 입니다.")

  def show_sortedlist(self): #지출 및 수입 순위 출력
    print("보고싶은 내역을 선택하세요")
    button = input("1번 - 수입, 2번 - 지출: ")#수입 혹은 지출 선택
    if(button == "1"):#주의 - button값은 input으로 받아 char형 변수임
      print("현재까지의 수입 순위")
      sortedlist = sorted(self.income_list)[::-1] #수입 리스트 정렬
      for i in range(0,10):#10위 까지만 출력
        if(len(self.income_list) <= i):#만약 리스트 크기보다 작을 경우 탈출
          break
        print(i+1,"위:",sortedlist[i],"원")
    elif(button == "2"):
      print("현재까지 사용한 금액 순위")
      sortedlist = sorted(self.spend_list)[::-1]#지출 리스트 정렬
      for i in range(0,10):#10위 까지만 출력
        if(len(self.income_list) <= i):#만약 리스트 크기보다 작을 경우 탈출
          break
        print(i+1,"위 ",sortedlist[i],"원")
    else:
      print("잘못 입력하셨습니다.")


  """
  고정 지출 리스트에 정보 추가 함수
  @Param
   spend_money : 지출 금액
   spend_date : 지출 날짜
  @Return
    None
  """
  def fixed_spend(self, spend_money, spend_date):  # 고정 지출 입력
    if spend_money <= 0:
      print("지출 금액은 0보다 커야 합니다.")
      return
    if spend_money > self.bal:
      print("잔액보다 큰 금액은 지출할 수 없습니다.")
      return        
    # 지출 리스트에 지출 정보 추가
    self.fixed_list.append((spend_money, spend_date))
    print(f"{spend_date}에 {spend_money}원의 고정 지출이 기록되었습니다.")
  """
  고정 지출 처리 함수
  @Param
    None
  @Return
    None
  """
  def process_daily_expenses(self):  # 매일 지출 처리
    today = datetime.now().date()
    # 고정 지출 리스트에 기록했던 날짜와 현재 날짜를 비교하여 동일하면 처리
    for spend_money, expense_date in self.fixed_list:
      spend_date = datetime.strptime(expense_date, "%Y-%m-%d").date()
      if spend_date == today:
        if spend_money <= self.bal:
          self.bal -= spend_money
          print(f"{expense_date}에 {spend_money}원의 고정 지출이 자동으로 처리되었습니다.")
        else:
          print(f"{expense_date}에 처리하지 못한 고정 지출이 있습니다. 잔액이 부족합니다.")
