import hashlib #hashlib 사용
import calendar #calendar 모듈 사용

userdata = {} #아이디, 비밀번호 저장해둘 딕셔너리

def user_reg() : #회원가입
    id = input("id 입력: " ) #회원가입 시의 id 입력

    pw = input("password 입력: ") #회원가입 시의 pw 입력

    h = hashlib.sha256() #hashlib 모듈의 sha256 사용
    h.update(pw.encode()) #sha256으로 암호화
    pw_data = h.hexdigest() #16진수로 변환

    f = open('login.txt', 'wb') #login 파일 오픈

    userdata[id] = pw_data #key에 id값을, value에 비밀번호 값

    with open('login.txt', 'a', encoding='UTF-8') as fw: #utf-8 변환 후 login.txt에 작성
        for user_id, user_pw in userdata.items(): #딕셔너리 내에 있는 값을 모두 for문
            fw.write(f'{user_id} : {user_pw}\n') #key, value값을 차례로 login.txt파일에 저장

def show_calendar(): #달력 출력
    year = 2024 #년도
    month = 6 #월
    print(calendar.month(year,month)) #2024.6 달력 출력

    while(1):
        menu = input("1.다음달, 2.저번달, 3.전체 달력, 4.년도와 월 선택, 5.종료 :") #년도와 월 설정

        if menu == "1": #다음달 달력 출력
            month += 1 #다음달 = 현재달 + 1
            if month == 13: #12월 초과라면
                year += 1 #년도 + 1
                month = 1 #1월로 설정
            print(calendar.month(year,month)) #출력
            
        elif menu == "2": #저번달 달력 출력
            month -= 1 #저번달 = 현재달 - 1
            if month == 0: #1월 미만이라면
                year -= 1 #년도 - 1
                month = 12 #12월로 설정
            print(calendar.month(year,month)) #출력
        
        elif menu == "3": #전체 달력 출력
            print(calendar.calendar(year)) #출력
        
        elif menu == "4": #입력한 년도와 월의 달력 출력
            year = int(input("년도 입력:")) #년도 입력
            month = int(input("월 입력:")) #월 입력
            print(calendar.month(year,month)) #출력
        
        elif menu == "5": #종료
            break

        else: #메뉴 선택 오류
            print("다시 선택해 주세요")


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
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

