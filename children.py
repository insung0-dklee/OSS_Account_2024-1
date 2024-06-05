def input_children_info():
    children_allowance.clear()
    num_children = int(input("아이의 숫자를 입력하세요: "))
    for i in range(num_children):
        name = input("아이의 이름을 입력하세요: ")
        children_allowance[name] = 0
    print("아이들의 정보가 성공적으로 입력되었습니다.")

def give_allowance():
    for name in children_allowance:
        allowance = float(input("{}에게 줄 용돈을 입력하세요: ".format(name)))
        children_allowance[name] += allowance
    print("용돈이 성공적으로 지급되었습니다.")

def check_allowance():
    print("\n아이들의 용돈:")
    for name, allowance in children_allowance.items():
        print("{}: {} 원".format(name, allowance))

# 아이들의 정보를 담을 딕셔너리 생성
children_allowance = {}

while True:
    print("\n1. 아이 정보 입력")
    print("2. 용돈 지급")
    print("3. 용돈 확인")
    print("4. 종료")
    choice = input("메뉴를 선택하세요: ")

    if choice == '1':
        input_children_info()
    elif choice == '2':
        give_allowance()
    elif choice == '3':
        check_allowance()
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴를 선택하세요.")
