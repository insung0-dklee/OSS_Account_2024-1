import tkinter as tk #tkinter 사용
from tkinter import messagebox
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
#숫자 여부를 판단하다
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def submit():   
# 입력 상자의 내용을 가져옵니다.
    name = name_entry.get()
    money = money_entry.get()
    if not is_number(money):
        messagebox.showerror("error", "숫자가 아님이다！")
        return
    print(f"상품: {name}, 가격: {money}")
    root.quit()
# GUI
def create_window():
    global name_entry, money_entry, root
# logo
    root = tk.Tk()
    root.title("제품정보")
    root.geometry("300x200")
# 입력
    name_label = tk.Label(root, text="제품")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)
# 입력
    money_label = tk.Label(root, text="가격")
    money_label.pack(pady=5)
    money_entry = tk.Entry(root)
    money_entry.pack(pady=5)
# 제출button
    submit_button = tk.Button(root, text="제출", command=submit)
    submit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_window()

