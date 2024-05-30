
b_is_exit = 0
# dates = [[2024, 5, 3],[2021, 3, 5]] 이런식으로 저장하는 리스트
dates = [] # 날짜를 기록하는 list

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        year = int(input("년도 입력(eg.2024): "))
        month = int(input("월 입력(eg. 5): "))
        day = int(input("날짜 입력(eg.30): "))
        
        # 입력된 값으로 리스트 생성
        # date[0] = year, date[1] = month, date[2] = day
        date = [year, month, day]
        dates.append(date)  # 날짜를 리스트에 추가

        # 날짜 출력 
        # dates는 리스트는 연도, 월, 일을 한 묶음으로 저장
        # 이 for loop은 리스트의 각 요소(year, month, day)를 돌면서 date의 변수에 할당
        print("기록된 날짜1:")
        for date in dates:
            print(f"{date[0]}년 {date[1]}월 {date[2]}일")  
       

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("1 입력시 날짜 기록.")

        break

    else:
        b_is_exit = not b_is_exit

