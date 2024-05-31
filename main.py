import hashlib
import os
import json
from datetime import datetime
import pickle

# 사용자 정보를 저장하는 딕셔너리
userdata = {}

# 로그인한 사용자 정보를 저장하는 딕셔너리
logged_in_users = {}

# 로그인 여부를 확인하는 함수
def is_logged_in(user_id):
    return user_id in logged_in_users

# 회원가입 함수
def user_reg():
    id = input("ID 입력: ")
    pw = input("Password 입력: ")

    # 비밀번호를 해시화하여 저장
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_hashed = h.hexdigest()

    # 사용자 정보 저장
    userdata[id] = pw_hashed
    with open('userdata.txt', 'w') as f:
        json.dump(userdata, f)
    print("회원가입이 완료되었습니다.")

# 로그인 함수
def user_login():
    id = input("ID 입력: ")
    pw = input("Password 입력: ")

    # 저장된 사용자 정보를 불러옴
    with open('userdata.txt', 'r') as f:
        userdata = json.load(f)

    # 입력된 ID가 존재하고 비밀번호가 일치할 경우 로그인 성공
    if id in userdata and userdata[id] == hashlib.sha256(pw.encode()).hexdigest():
        logged_in_users[id] = True
        print("로그인 성공")
    else:
        print("로그인 실패")

# 로그아웃 함수
def user_logout(user_id):
    if is_logged_in(user_id):
        del logged_in_users[user_id]
        print("로그아웃 되었습니다.")
    else:
        print("로그인 상태가 아닙니다.")

# 사용자의 가계부 관리 함수
def manage_ledger(user_id):
    if is_logged_in(user_id):
        print(f"{user_id}의 가계부를 관리합니다.")
        # 이후 가계부 관리 기능을 구현할 수 있음
    else:
        print("로그인 상태가 아닙니다.")

# 메인 함수
def main():
    while True:
        print("\n1. 회원가입")
        print("2. 로그인")
        print("3. 로그아웃")
        print("4. 가계부 관리")
        print("5. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            user_reg()
        elif choice == "2":
            user_login()
        elif choice == "3":
            user_id = input("로그아웃할 사용자 ID 입력: ")
            user_logout(user_id)
        elif choice == "4":
            user_id = input("가계부를 관리할 사용자 ID 입력: ")
            manage_ledger(user_id)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()
