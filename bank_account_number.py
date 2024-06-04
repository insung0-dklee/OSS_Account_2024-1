class Account: # 이름, 계좌번호, 비밀번호 입력
  def __init__(self, name, account_number, password):
      self.name = name
      self.account_number = account_number
      while True: # 4자리 수 비밀번호를 입력하도록 함
          password_input = input("비밀번호를 다시 입력하세요 (4자리 숫자): ")
          if len(password_input) != 4 or not password_input.isdigit():
              print("비밀번호는 4자리 숫자로 입력해주세요.")
          else:
              self.password = password_input
              break

class AccountRegistry:
  def __init__(self):
      self.accounts = {}

  def add_account(self, name, account_number, password):
      if name in self.accounts: # 이미 이름이 등록 되어 있을 시
          print(f"이미 등록된 이름입니다: {name}")
          return
      if account_number in [account.account_number for account in self.accounts.values()]:
          print(f"이미 등록된 계좌번호입니다: {account_number}")
          return # 이미 계좌번호가 등록 되어 있을 시
      self.accounts[name] = Account(name, account_number, password)
      print(f"{name}의 계좌 ({account_number})가 등록되었습니다.")
      # 입력 계좌 등록

  def find_account(self, name): 
      return self.accounts.get(name, None)

def main():
  registry = AccountRegistry()

  # 친구 등록
  while True:
      name = input("저장하고 싶은 계좌주의 이름을 입력하세요 (종료하려면 '종료' 입력): ")
      if name == "종료":
          break
      account_number = input(f"{name}의 계좌번호를 입력하세요: ")
      password = input(f"{name}의 비밀번호를 입력하세요: ") # 비밀번호 추가 
      registry.add_account(name, account_number, password) # 비밀번호 전달

  # 계좌 찾기
  while True:
    search_name = input("찾고 싶은 계좌주의 이름을 입력하세요 (종료하려면 '종료' 입력): ")
    if search_name == "종료":
        break
        
    account = registry.find_account(search_name)
    if account:
        while True: # 계좌 비밀번호 입력 및 확인
            password1 = input(f"{name}의 계좌 비밀번호를 입력하세요: ") 
            password2 = input(f"{name}의 계좌 비밀번호를 다시 입력하세요: ")
            if password1 == password2:
                if password1 == account.password: 
                    print(f"{account.name}의 계좌번호: {account.account_number}")
                    break # 비밀번호 일치 시 종료
                if password1 != password2:
                    print("비밀번호가 일치하지 않습니다. 다시 시도하세요.")
                    continue # 비밀번호 불일치 시 다시 시도
                else:
                    print ("비밀번호가 틀립니다.")
                    continue # 비밀번호 틀릴 시 다시 시도
                
    else: # 계좌 찾기 실패 시
         print("해당하는 계좌를 찾을 수 없습니다.")

if __name__ == "__main__":
  main() # 메인 함수 호출
