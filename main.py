def show_help():
    print("도움말:")
    print("1: 가계부 항목 기입")
    print("2: 가계부 항목 보기")
    print("3: 가계부 항목 삭제")
    print("?: 도움말 보기")
    print("exit: 프로그램 종료")
# 기능을 모르는 분들한테 도움을 주기위해 추가했습니다.

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        show_help()
        # ?를 입력하면 기능이 무엇인지 알려줍니다.
        break

    else:
        b_is_exit = not b_is_exit

