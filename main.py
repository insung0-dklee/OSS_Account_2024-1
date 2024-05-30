import hashlib #hashlib 사용

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

    elif func == "?": # '?' 입력시 안내문 나오도록 함수 추가
        print_help()

        break

    else:
        b_is_exit = not b_is_exit

