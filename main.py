import hashlib

def login():
    # 사용자로부터 ID 입력받기
    print("id 입력:", end=" ")
    id = input()

    # 사용자로부터 비밀번호 입력받기
    print("password 입력:", end=" ")
    pw = input()

    # 비밀번호를 SHA-256 해시로 변환
    h = hashlib.sha256()
    h.update(pw.encode())  # 입력받은 비밀번호를 인코딩하여 해시 객체에 업데이트
    pw_data = h.hexdigest()  # 해시 값을 16진수 문자열로 변환

    # 'login.txt' 파일을 읽기 모드로 열기
    f = open('login.txt', 'r')

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":
        login()
        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

