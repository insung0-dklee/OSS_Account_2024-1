def set_total_budget():
    global total_budget
	#전역변수로 예산을 지정해 예산 확인 함수에도 사용
    total_budget = float(input("예산을 입력하세요: "))
    print(f"예산은 {total_budget}원 입니다.")

def check_total_budget():
    if total_budget is None:
        print("예산이 지정되지 않았습니다.")
    else:
        print(f"현재 예산은 {total_budget}원 입니다.")

global total_budget
total_budget = None
b_is_exit = 0
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말, 0 입력시 종료) : ")

    if func == "1":

        pass

    elif func == "2":
        pass

    elif func == "3":
         pass

    elif func == "4":
        # 예산 설정 및 재설정
        set_total_budget()
    
    elif func == "5":
        # 예산 확인
        check_total_budget()
    
    elif func == "?":
        print("도움말")
        print("1: ")
        print("2: ")
        print("3: ")
        print("4: 예산 설정 및 재설정")
        print("5: 예산 확인")
        print("0: 종료")
    
    elif func == "0":
        b_is_exit = 1
    
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
