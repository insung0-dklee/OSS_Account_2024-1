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

def user_login():  # 로그인 함수
    id = input("id 입력: ")  # 로그인 시 id 입력
    pw = input("password 입력: ")  # 로그인 시 pw 입력

    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    if id in userdata and userdata[id] == pw_data:
        print("로그인 성공")
        return True
    else:
        print("로그인 실패")
        return False

def user_logout():  # 로그아웃 함수
    print("로그아웃 되었습니다.")

b_is_exit = 0
is_logged_in = False  # 로그인 상태를 저장하는 변수

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

