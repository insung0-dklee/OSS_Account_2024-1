

b_is_exit = 0

def print_help():
    # 도움말 메시지 출력 함수
    # 이 함수는 사용자가 사용할 수 있는 각 기능에 대한 설명을 출력
    print("1: ??") # 1번을 누르면 수입 추가 등 안내문 출력
    print("2: ??")
    print("3: ??")
    print("4: ??")
    print("?: ??")

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

