

b_is_exit = 0
money = 0 #현재 잔고를 표시하는 money 변수를 0으로 초기화화
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("지출") #func이 1일때 지출을 확인인하는 부분
        where = input("어디에 썼나요?") #지출이 나간 장소를 쓰는 코드 / where이라는 변수에 장소를 저장
        exp = float(input("얼마나 썼나요?(숫자만 쓰세요)")) #얼마를 썼는지 저장하는 함수 / exp라는 변수에 지출한 금액 저장장
        money -= exp #잔고를 표시하는 money 변수에 지출 금액을 나타낸 exp 변수를 빼주는 코드
        print(exp, "만큼 소비했습니다.") #소비한 지출 금액인 exp 변수를 이용해 소비 금액을 표시해주는 코드
        break

    elif func == "2":
        print("저축") #func이 2일때 저축을 확인인하는 부분
        sav = float(input("얼마를 저축했나요?(숫자만 쓰세요)")) #얼마를 저축했는지 저장하는 함수 / sav라는 변수에 지출한 금액 저장장
        money += sav #잔고를 표시하는 money 변수에 저축 금액을 나타낸 sav 변수를 더해주는 코드
        print(sav, "만큼 저축했습니다.") #저축한 금액인 sav 변수를 이용해 저축 금액을 표시해주는 코드
        break

    elif func == "3":
        print("잔고") #func이 3일때 잔고를 확인하는 부분
        print(money, "만큼의 잔고가 있습니다") #money 변수를 이용해 잔고를 표시해주는 코드
        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit