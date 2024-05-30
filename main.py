def main():
    balance = 0 # 보유금액 변수 지정 및 0으로 초기값을 준다.

    while True: #값이 Ture일 때까지 계속 반복한다.
        print("1 : 더하기 / 2 : 빼기 / 3 : 종료 / 4 : 도움") # 1은 더하기, 2는 빼기, 3은 종료, 4는 도움을 프린트한다.
        print(f"현재 보유금액은 {balance}입니다.") # 보유금액을 먼저 출력한다.
        want = input("원하는 작업 번호를 선택하세요: ") # want변수를 지정하고 input을 이용해서 번호를 받는다.

        if want == '1': # want의 값이 1일 때 사용된다.
            money = float(input("금액을 입력하세요: ")) # moeny변수를 지정하고 float으로 실수형을 받고 input으로 money 변수에 값을 넣는다.
            balance += money # 보유금액인 balance와 money를 더한다.
            print(f"현재 보유금액은 {balance}입니다.") # 보유금액을 프린트한다.
        elif want == '2': # want의 값이 2일 때 사용된다. 
            money = float(input("금액을 입력하세요: ")) # moeny변수를 지정하고 float으로 실수형을 받고 input으로 money 변수에 값을 넣는다.
            if money > balance: # 입력받은 money의 값이 balance 즉 보유금액 보다 작을 경우를 뜻한다.
                print("잔액이 부족합니다.") # 보유금액이 마이너스가 될 수 없기 때문에 잔액이 부족하다고 뜬다.
            else: # 보유금액에서 입력받은 값을 뺄 수 있을 때
                balance -= money #  보유금액인 balance 에서 입력받은 money를 뺀다.
                print(f"현재 보유금액은 {balance}입니다.") # 보유금액을 출력한다.
        elif want == '3': # want의 값이 3일 때 사용된다.
            print("프로그램을 종료합니다.") # 프로그램을 종료합니다.가 출력된다.
            break # 프로그램을 종료한다.
        elif want == '4': # want의 값이 4일 때 사용된다. 
            print("도움말: 프로그램은 다음과 같은 기능을 제공합니다.") # 문장을 프린트한다.
            print("1 : 더하기 - 금액을 보유금액에 추가합니다.") # 문장을 프린트한다.
            print("2 : 빼기 - 금액을 보유금액에서 차감합니다.") # 문장을 프린트한다.
            print("3 : 종료 - 프로그램을 종료합니다.") # 문장을 프린트한다.
            print("4 : 도움 - 이 도움말을 표시합니다.") # 문장을 프린트한다.
        else: # want의 값이 1,2,3,4가 아닌 다른 것일 경우에 작동한다.
            print("잘못된 선택입니다. 다시 시도하세요.") # 프린트한다.

if __name__ == "__main__":
    main()
