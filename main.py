import os
import hashlib
import shutil
from datetime import datetime

userdata = {}  # 사용자 데이터 저장
couple_data = {}  # 커플 데이터 저장

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except FileNotFoundError:
        print("오류: 파일을 찾을 수 없습니다.")
    except PermissionError:
        print("오류: 파일에 대한 권한이 없습니다.")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def user_reg():
    id = input("id 입력: ")
    pw = input("password 입력: ")
    
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()

    userdata[id] = pw_data

    with open('login.txt', 'a', encoding='UTF-8') as fw:
        fw.write(f'{id} : {pw_data}\n')
    print("회원가입이 완료되었습니다.")

def couple_reg():
    print("커플통장 회원가입:")
    user1_id = input("첫 번째 사용자 id 입력: ")
    user2_id = input("두 번째 사용자 id 입력: ")
    start_date = input("사귀기 시작한 날짜를 입력하세요 (YYYY-MM-DD): ")

    try:
        datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        print("날짜 형식이 올바르지 않습니다. 다시 시도해주세요.")
        return

    if user1_id in userdata and user2_id in userdata:
        couple_key = f"{user1_id}-{user2_id}"
        couple_data[couple_key] = start_date

        with open('couple_data.txt', 'a', encoding='UTF-8') as fw:
            fw.write(f'{couple_key} : {start_date}\n')

        print("커플통장이 성공적으로 등록되었습니다.")
    else:
        print("두 사용자 모두 회원가입되어 있어야 합니다.")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        user_reg()

    elif func == "2":
        couple_reg()

    elif func == "3":
        print("기능 3 실행.")
        # 기능 3을 위한 코드 추가

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1 - 회원가입, 2 - 커플통장 회원가입, 3 - 기능 3, '복사' - 파일 복사, '종료' - 종료")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
