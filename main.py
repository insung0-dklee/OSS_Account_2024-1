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
"""
add_memo : 파일 입출력을 사용하여 메모장을 추가할 수 있는 기능으로 예상지출내역, 오늘의 목표등을 기록할 수 있다.
@Parm
    None
@Return
    None
"""
def add_memo():
    print("메모장 제목: ")
    str_title = input()
    new_f = open(str_title,"w",encoding="utf8")
    print("내용 입력: ")
    str_memo = input()
    new_f.write(str_memo)
    new_f.close()

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break
    elif func == "메모장":
        add_memo()
        break
    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

