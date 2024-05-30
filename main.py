import hashlib #hashlib 사용
import Account_book

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

b_is_exit = 0
#가계부 초깃값 임의로 설정
a = Account_book("가계부 1",1000000)
b = Account_book("가계부 2",2000000)
c = Account_book("가계부 3",3000000)

Account_list = [a,b,c] #가계부 리스트
i=0

def choose_Account(func):#가계부 선택 함수
    print("가계부 선택(번호로 입력)")
    for i in range(0,len(Account_list)):#가계부 리스트 출력
      print(f"가계부 {i+1}번 : ",Account_list[i].name)
    choose = input()
    return choose 

while not b_is_exit:
    print("--------------------------------")
    choose = int(choose_Account(func))-1
    func = input("기능 입력 (? 입력시 도움말) : ")

    if choose > len(Account_list):
      print("해당하는 가계부가 없습니다.")
      continue1
    if func == "1":
      Account_list[choose].income()
    elif func == "2":
      Account_list[choose].spend()
    elif func == "3":
      Account_list[choose].show_account()
      Account_list[choose].show_total()
    elif func == "4":
      Account_list[choose].show_sortedlist()
    elif func == "?":
        print("도움말 입력.");
    else:
        b_is_exit = not b_is_exit
        print("프로그램을 종료합니다.");
        break


